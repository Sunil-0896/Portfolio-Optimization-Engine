import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QGraphicsScene,QCompleter
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from projects.MC_simulate_random_weights.simulation_py import Ui_MainWindow
from projects.MC_simulate_random_weights.GBM import GBM_
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as figurecanvas
import io
import matplotlib.pyplot as plt
import yfinance as yf

class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.global_tickers = [
    "NVDA",   # NVIDIA Corporation
    "AAPL",   # Apple Inc.
    "GOOGL",  # Alphabet Inc. (Class A)
    "MSFT",   # Microsoft Corporation
    "AMZN",   # Amazon.com, Inc.
    "TSM",    # Taiwan Semiconductor Manufacturing
    "META",   # Meta Platforms, Inc.
    "AVGO",   # Broadcom Inc.
    "2222.SR",# Saudi Aramco (Tadawul)
    "TSLA",   # Tesla, Inc.
    "BRK-B",  # Berkshire Hathaway (Class B)
    "WMT",    # Walmart Inc.
    "LLY",    # Eli Lilly and Company
    "JPM",    # JPMorgan Chase & Co.
    "XOM",     # Exxon Mobil Corporation
    "RELIANCE",   # Reliance Industries
    "HDFCBANK",   # HDFC Bank
    "BHARTIARTL", # Bharti Airtel
    "SBIN",       # State Bank of India
    "ICICIBANK",  # ICICI Bank
    "TCS",        # Tata Consultancy Services
    "INFY",       # Infosys
    "BAJFINANCE", # Bajaj Finance
    "HINDUNILVR", # Hindustan Unilever
    "LT",         # Larsen & Toubro
    "SUNPHARMA",  # Sun Pharmaceutical
    "MARUTI",     # Maruti Suzuki
    "AXISBANK",   # Axis Bank
    "HCLTECH",    # HCL Technologies
    "ITC"         # ITC Limited
]

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.initial.valueChanged.connect(self.update)
        self.ui.no_of_days.valueChanged.connect(self.update)
        self.ui.no_of_sims.valueChanged.connect(self.update)

        self.ui.simulate_button.clicked.connect(self.plot)
        self.set_auto(self.ui.comboBox_stock)
        self.ui.comboBox_stock.currentTextChanged.connect(self.download_data)
        
    
        
    def update(self):
        self.initial = self.ui.initial.value()
        self.no_of_days = self.ui.no_of_days.value()
        self.no_of_sims = self.ui.no_of_sims.value()
        self.ui.textBrowser.setText('Initial Amount : ' + str(self.initial))
        self.ui.textBrowser.append('No_of_days : ' + str(self.no_of_days))
        self.ui.textBrowser.append('No_of_Sims : ' + str(self.no_of_sims))

    def download_data(self):
        stock = self.ui.comboBox_stock.currentText()
        data = yf.download(stock,'2023-01-01','2026-03-01')
        self.data = data['Close']

    def set_auto(self,box):
        box.addItems(self.global_tickers)
        qcomp = QCompleter(self.global_tickers)
        qcomp.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        box.setCompleter(qcomp)

    def plot(self):
        price_final = GBM_(self.data,self.initial,self.no_of_sims,self.no_of_days)

        fig,ax = plt.subplots()
        ax.plot(price_final)
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        plt.close()

        pixmap = QPixmap()
        pixmap.loadFromData(buf.getvalue())

        size_of_scene = self.ui.graphicsView.size()
        scaled_pixmap = pixmap.scaled(size_of_scene)
        self.scene = QGraphicsScene()
        self.scene.addPixmap(scaled_pixmap)
        self.ui.graphicsView.setScene(self.scene)
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    window = Main_window()
    window.show()
    sys.exit(app.exec())
