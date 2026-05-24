"""Generate a sample deck with one slide for each chart type."""

from charts import (
    new_deck,
    add_bar_callout,
    add_stacked_bar_over_time,
    add_waterfall,
)

OUT = "test_output.pptx"


def main():
    prs = new_deck()
    blank = prs.slide_layouts[6]

    # ---- Slide 1: TAM bar + callout ----
    slide = prs.slides.add_slide(blank)
    add_bar_callout(
        slide,
        title="RTD coffee TAM will hit $42.5B by 2028, growing 8.6% CAGR",
        categories=["2023", "2024", "2025", "2026", "2027", "2028"],
        values=[28.1, 30.8, 33.6, 36.5, 39.4, 42.5],
        highlight_index=5,
        callout="$42.5B\n2028 TAM",
        y_label="USD, billions",
        source="Euromonitor 2025; Mintel; team analysis",
    )

    # ---- Slide 2: Stacked revenue mix over time ----
    slide = prs.slides.add_slide(blank)
    add_stacked_bar_over_time(
        slide,
        title="Enterprise segment now drives 62% of revenue, up from 18% in 2021",
        categories=["FY21", "FY22", "FY23", "FY24", "FY25"],
        series=[
            ("SMB",        [12, 14, 15, 16, 18]),
            ("Mid-market", [8,  12, 16, 22, 28]),
            ("Enterprise", [4,  10, 22, 38, 74]),
        ],
        highlight_series="Enterprise",
        y_label="Revenue, $M",
        source="Internal financials; FY21–FY25",
    )

    # ---- Slide 3: Revenue waterfall ----
    slide = prs.slides.add_slide(blank)
    add_waterfall(
        slide,
        title="FY24 → FY25 revenue bridge: $80M → $112M, with new logos doing the heavy lifting",
        labels=["FY24",   "New logos", "Expansion", "Churn", "Price", "FY25"],
        values=[80.0,     24.0,         12.0,        -8.0,    4.0,     112.0],
        kinds=["start",   "pos",        "pos",       "neg",   "pos",   "total"],
        y_label="Revenue, $M",
        source="Internal financials; FY24–FY25",
    )

    prs.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
