import flet as ft
import pandas as pd
from typing import Optional

class DashboardApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.df: Optional[pd.DataFrame] = None
        
    def build(self):
        # ファイルドロップエリア
        self.drop_zone = ft.Container(
            content=ft.Text("ここにCSVファイルをドロップ"),
            width=200,
            height=200,
            bgcolor=ft.colors.BLUE_50,
            border=ft.border.all(2, ft.colors.BLUE_400),
            border_radius=ft.border_radius.all(10),
            padding=ft.padding.all(20),
            alignment=ft.alignment.center,
        )

        # グラフエリア
        self.chart = ft.LineChart(
            expand=True,
            tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
            min_y=0,
            animate=1000,
        )

        # データテーブル
        self.data_table = ft.DataTable(
            columns=[],
            rows=[],
        )

        # 統計情報
        self.stats_view = ft.Column(
            controls=[
                ft.Text("基本統計情報", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("データ件数: -"),
                ft.Text("合計値: -"),
                ft.Text("平均値: -"),
            ]
        )

        return ft.Column(
            controls=[
                ft.AppBar(
                    title=ft.Text("データ可視化ダッシュボード"),
                    bgcolor=ft.colors.BLUE_700,
                ),
                ft.Row(
                    controls=[self.drop_zone, self.chart],
                    expand=True,
                ),
                self.data_table,
                self.stats_view,
            ],
            expand=True,
        )

def main(page: ft.Page):
    page.title = "データ可視化ダッシュボード"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(DashboardApp())

ft.app(target=main)