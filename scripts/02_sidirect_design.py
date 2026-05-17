from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Bio import SeqIO
import pandas as pd
import time
import os


# ============================
# PATHS
# ============================

FASTA_FILE = "../data/IL6_mRNA.fasta"

OUTPUT_FILE = "../results/siRNA_candidates.csv"


# ============================
# READ FASTA
# ============================

record = SeqIO.read(
    FASTA_FILE,
    "fasta"
)

sequence = str(record.seq)
reference = record.id


# ============================
# CHROME SETUP
# ============================

options = webdriver.ChromeOptions()

options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(

    service=Service(
        ChromeDriverManager().install()
    ),

    options=options

)

wait = WebDriverWait(
    driver,
    20
)


# ============================
# OPEN siDirect
# ============================

driver.get(
"https://sidirect2.rnai.jp/"
)

textarea = wait.until(

EC.presence_of_element_located(
(By.TAG_NAME,"textarea")
)

)

textarea.clear()

textarea.send_keys(sequence)


submit = driver.find_elements(
By.XPATH,
"//input[@type='submit']"
)[-1]

driver.execute_script(
"arguments[0].click();",
submit
)


WebDriverWait(driver,15).until(

lambda d:
"Effective siRNA candidates"
in d.page_source

)


time.sleep(2)


# ============================
# SCRAPE RESULTS
# ============================

rows_out = []

tables = driver.find_elements(
By.TAG_NAME,
"table"
)


for table in tables:

    rows = table.find_elements(
        By.TAG_NAME,
        "tr"
    )

    for row in rows[1:]:

        cols = row.find_elements(
            By.TAG_NAME,
            "td"
        )

        if len(cols) < 7:
            continue


        vals = [
            c.text.strip()
            for c in cols
        ]


        rows_out.append({

            "Reference":

            reference,


            "Target_position":

            vals[0],


            "Target_sequence":

            vals[1],


            "Functional_score":

            vals[2],


            "Guide":

            vals[3],


            "Passenger":

            vals[4],


            "Tm_guide":

            vals[5],


            "Tm_passenger":

            vals[6]

        })


driver.quit()


# ============================
# SAVE CSV
# ============================

df = pd.DataFrame(
rows_out
)

df.to_csv(

OUTPUT_FILE,

index=False

)


print(
f"Saved {len(df)} candidates"
)

print(
f"Output → {OUTPUT_FILE}"
)