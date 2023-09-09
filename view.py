from PySide6.QtWidgets import *
import sys
import model


class ExchangeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Exchange Rate App")
        self.setGeometry(100, 100, 300, 300)
        main_layout = QVBoxLayout()

        sub_main_layout = QVBoxLayout()
        sub_requested_layout = QVBoxLayout()
        main_currency_layout = QHBoxLayout()
        requested_currency_layout = QHBoxLayout()

        # Result and Edit field Design
        self.main_cur_exp = QLabel()
        self.result_field = QLineEdit()
        self.result_field.setReadOnly(True)
        self.result_field.setPlaceholderText("Press Calculate to see result")
        self.requested_cur_exp = QLabel()
        self.edit_field = QLineEdit()
        self.edit_field.setPlaceholderText("Choose Currency and write amount")
        self.edit_field.textChanged.connect(self.main_amount_changed)

        # Drop Down Button Design
        self.main_choose_cur_button = QComboBox()
        self.main_choose_cur_button.addItems(model.currency_list)
        self.main_choose_cur_button.currentTextChanged.connect(self.main_currency_changed)

        self.requested_choose_cur_button = QComboBox()
        self.requested_choose_cur_button.addItems(model.currency_list)
        self.requested_choose_cur_button.currentTextChanged.connect(self.requested_currency_changed)

        # Calculate Button Design
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.get_amount)

        sub_requested_layout.addWidget(self.requested_cur_exp)
        requested_currency_layout.addWidget(self.result_field)
        requested_currency_layout.addWidget(self.requested_choose_cur_button)
        sub_requested_layout.addLayout(requested_currency_layout)
        sub_main_layout.addWidget(self.main_cur_exp)
        main_currency_layout.addWidget(self.edit_field)
        main_currency_layout.addWidget(self.main_choose_cur_button)
        sub_main_layout.addLayout(main_currency_layout)

        main_layout.addLayout(sub_main_layout)
        main_layout.addLayout(sub_requested_layout)
        main_layout.addWidget(self.calculate_button)

        self.container = QWidget()
        self.container.setLayout(main_layout)
        self.setCentralWidget(self.container)
        self.resize(600, 600)
        self.show()


    def get_amount(self):
        if float(self.edit_field.text()):
            model.result_currency = float(self.edit_field.text())
            self.result_field.setText(str(format(model.make_request() * model.result_currency, ".2f")))
        else:
            self.edit_field.setText("1.0")

    def main_amount_changed(self, s):
        model.main_amount = s

    def main_currency_changed(self, s):
        model.main_currency = s
        self.main_cur_exp.setText(model.get_exp(s))

    def requested_currency_changed(self, s):
        model.requested_currency = s
        self.requested_cur_exp.setText(model.get_exp(s))




app = QApplication(sys.argv)
# Create a Qt widget, which will be our window.
window = ExchangeApp()
window.show()
# Start the event loop.
app.exec()
