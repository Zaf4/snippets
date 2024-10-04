from lets_plot import element_blank, element_text, theme

theme(
    text=element_text(color="#1f1f1f", family="Segoe UI", size=13),
    legend_title=element_text(face="bold"),
    title=element_text(color="#1f1f1f", family="Segoe UI"),
    plot_title=element_text(face="bold", size=22),
    plot_subtitle=element_text(size=18),
    panel_grid=element_blank(),
)
