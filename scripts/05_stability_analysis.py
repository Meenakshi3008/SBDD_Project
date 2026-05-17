import pandas as pd

sirna=pd.read_csv(
"../results/ranked_siRNA.csv"
)

regions=pd.read_csv(
"../results/accessible_regions.csv"
)


def accessible(pos):

    try:

        parts=str(pos).split("-")

        if len(parts)<2:
            return 0

        start=int(parts[0])
        end=int(parts[1])

        for _,r in regions.iterrows():

            if (
            start<=r["end"]
            and
            end>=r["start"]
            ):
                return 1

        return 0

    except:
        return 0


sirna["Accessibility"]=(
sirna["Target_position"]
.apply(accessible)
)

sirna["Final_score"]=(
sirna["Tm_difference"]*0.6
+
sirna["Accessibility"]*5
)

ranked=sirna.sort_values(
"Final_score",
ascending=False
)

ranked.to_csv(
"../results/final_ranked_siRNA.csv",
index=False
)

print(

ranked[
[
"Target_position",
"Tm_difference",
"Accessibility",
"Final_score"
]
].head()

)

print("Saved")