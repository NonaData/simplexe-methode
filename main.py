import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from fractions import Fraction

class Simplexe(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Méthode Simplex Calculateur")
        self.resize(1100, 800)
        self.center_window()
        self.setupUI()

# ******************************** Interface graphique ************************************ #

    def center_window(self):
        # Center the window on the screen:
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        x = (screen_geometry.width() // 2) - (self.width() // 2)
        y = (screen_geometry.height() // 2) - (self.height() // 2)
        self.setGeometry(x, y, self.width(), self.height())

    def setupUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.main_widget = QWidget(self)
        main_layout = QVBoxLayout()
        self.main_widget.setLayout(main_layout)

        self.setup_scroll_area(layout)
        self.setup_header_widget()

        # Spacer above the form widget:
        top_spacer = QWidget()
        top_spacer.setFixedHeight(100)
        main_layout.addWidget(top_spacer)

        self.setup_form_widget()

        # Spacer below the form widget:
        bottom_spacer = QWidget()
        bottom_spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        main_layout.addWidget(bottom_spacer)

        self.form_widget_2 = None
        self.All_Tables_widget = None

        # All rights reserved label:
        self.rights_reserved_label = QLabel("@2024 All rights are reserved to NonaData team.")
        self.rights_reserved_label.setStyleSheet("color: #999; font-size: 14px; font-style: italic;")
        self.rights_reserved_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.rights_reserved_label)

    def setup_scroll_area(self, layout):
        # Set up the scroll area for the main widget:
        scroll_area = QScrollArea(self)
        scroll_area.setWidget(self.main_widget)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

    def setup_header_widget(self):
        # Setup the header section with images and labels:
        self.header_widget = QWidget(self.main_widget)
        self.header_widget.setFixedHeight(200)
        header_layout = QGridLayout()
        header_layout.setContentsMargins(10, 10, 10, 10)
        self.header_widget.setLayout(header_layout)

        self.add_image_to_header(header_layout, "images/NonaData.png", Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, 0, 0)
        self.add_centered_text_to_header(header_layout, "Méthode Simplex Calculateur", 0, 1)
        self.add_image_to_header(header_layout, "images/ensao.png", Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight, 0, 2)

        self.main_widget.layout().addWidget(self.header_widget)

    def add_image_to_header(self, layout, image_path, alignment, row, col):
        # Add an image to the header section:
        label = QLabel(self.header_widget)
        pixmap = QPixmap(image_path).scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.setAlignment(alignment)

        # Set up event filter to detect hover events:
        label.setAttribute(Qt.WidgetAttribute.WA_Hover)
        label.installEventFilter(self)

        layout.addWidget(label, row, col)

    def add_centered_text_to_header(self, layout, text, row, col):
        # Add a centered text label to the header:
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(self.get_text_label_style())

        # Set up event filter to detect hover events:
        label.setAttribute(Qt.WidgetAttribute.WA_Hover)
        label.installEventFilter(self)

        layout.addWidget(label, row, col)

    def eventFilter(self, obj, event):
        # Detect hover events and add/remove shadow effect:
        if event.type() == QEvent.Type.HoverEnter:
            self.add_shadow_effect(obj)
        elif event.type() == QEvent.Type.HoverLeave:
            self.remove_shadow_effect(obj)
        return super().eventFilter(obj, event)

    def add_shadow_effect(self, widget):
        # Add shadow effect to the widget.
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(5, 5)
        shadow.setColor(Qt.GlobalColor.gray)
        widget.setGraphicsEffect(shadow)

    def remove_shadow_effect(self, widget):
        # Remove shadow effect from the widget.
        widget.setGraphicsEffect(None)

    def get_text_label_style(self):
        # Return the common style for header text.
        return """
            font-size: 28px;
            font-weight: bold;
            color: #4CAF50;
            padding: 10px;
        """

    def setup_form_widget(self):
        self.form_widget_1 = QWidget(self.main_widget)
        self.form_widget_1.setFixedHeight(250)
        self.form_widget_1.setStyleSheet("""
            QWidget{
                padding: 20px;
                border-radius: 10px;
                background-color: #f5f5f5;
            }
            QLabel{
                padding: 5px;
                font-size: 16px;
                font-weight: bold;
                color: #333;
            }

            QSpinBox {
                padding: 5px;
                font-size: 14px;
                background-color: #fff;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        # Shadow effect:
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(3, 3)
        shadow.setColor(Qt.GlobalColor.gray)
        self.form_widget_1.setGraphicsEffect(shadow)

        # Create a vertical layout to center content:
        self.vertical_layout = QVBoxLayout(self.form_widget_1)
        self.vertical_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a form layout to add widgets:
        self.form_layout_1 = QFormLayout()
        self.vertical_layout.addLayout(self.form_layout_1)

        # Variables spinbox:
        self.variables_spinbox = QSpinBox(self.form_widget_1)
        self.variables_spinbox.setMinimum(1)
        self.variables_spinbox.setMaximum(10)
        self.variables_spinbox.setToolTip("Valeur maximale est 10")
        self.variables_spinbox.setStyleSheet("""
            QSpinBox::up-button, QSpinBox::down-button {
                border: none;
            }
        """)
        self.form_layout_1.addRow(QLabel("<div style='font-size: 25px'>Nombre des variables:</div>"), self.variables_spinbox)

        # Constraints spinbox:
        self.constraint_spinbox = QSpinBox(self.form_widget_1)
        self.constraint_spinbox.setMinimum(1)
        self.constraint_spinbox.setMaximum(10)
        self.constraint_spinbox.setToolTip("Valeur maximale est 10")
        self.constraint_spinbox.setStyleSheet("""                   
            QSpinBox::up-button, QSpinBox::down-button {
                border: none;
            }
        """)
        self.form_layout_1.addRow(QLabel("<div style='font-size: 25px'>Nombre des contraintes:</div>"), self.constraint_spinbox)

        # Add an explanatory label
        self.max_values_label = QLabel("<div style='font-size: 15px'>La valeur maximale pour les variables et les contraintes est 10.</div>")
        self.max_values_label.setStyleSheet("color: #666; font-size: 12px; font-style: italic;")
        self.max_values_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vertical_layout.addWidget(self.max_values_label)

        # Reset and Submit buttons:
        self.generate_button = QPushButton("Générer", clicked=lambda: self.Saisir_Donnee())
        self.reset_button = QPushButton("Réinitialiser", clicked=lambda: self.reset(True))

        self.generate_button.setStyleSheet("""
            QPushButton {
                padding: 10px 20px;
                margin: 10px;
                color: white;
                font-size: 20px;
                background-color: #29bec5;
                border-radius: 5px;
                border: 2px solid transparent;
            }
            QPushButton:hover {
                color: #29bec5;
                background-color: white;
                border: 2px solid #29bec5;
            }
            QPushButton:pressed {
                color: white;
                background-color: #29bec5;
            }
        """)

        self.reset_button.setStyleSheet("""
            QPushButton {
                padding: 10px 20px;
                margin: 10px;
                color: white;
                font-size: 20px;
                background-color: #ff6c22;
                border-radius: 5px;
                border: 2px solid transparent;
            }
            QPushButton:hover {
                color: #ff6c22;
                background-color: white;
                border: 2px solid #ff6c22;
            }
            QPushButton:pressed {
                color: white;
                background-color: #ff6c22;
            }
        """)

        # Add buttons to the form layout
        self.form_layout_1.addRow(self.generate_button, self.reset_button)

        self.main_widget.layout().addWidget(self.form_widget_1)

        self.form_widget_2 = None

        return
    
    def Saisir_Donnee(self):                                                            

        self.reset(False)

        # > Form Pour Remplir les Donnée
        self.form_widget_2 = QWidget(self.main_widget)
        self.form_layout_2 = QFormLayout(self.form_widget_2)

        # > Fonction Objective Label
        label = QLabel("Fonction Objective:")
        label.setStyleSheet("font-size: 20px;color: black;")
        self.form_layout_2.addRow(label)  
        
        # > Fonction Objective Widget
        objective_function_widget = QWidget(self.form_widget_2)
        objective_function_widget.setLayout(QHBoxLayout())

        # > ComboBox for Maximiser et Minimiser 
        self.max_min_combobox = QComboBox(objective_function_widget)
        self.max_min_combobox.addItem("Maximiser")
        self.max_min_combobox.addItem("Minimiser")

        # > Style of ComboBox  
        self.max_min_combobox.setStyleSheet("""
                                            QComboBox {
                                                height: 40px;
                                                width: 130px;
                                                font-size: 20px;
                                                text-align: right;
                                                border-radius: 5px;
                                                border: 2px solid #3d3e3f;
                                            }
                                            QComboBox::drop-down:button {
                                                background-color: #29bec5;
                                                border: none;
                                            }
                                            
                                        """)
        # > Customize the dropdown menu:
        self.max_min_combobox.view()
        self.max_min_combobox.view().setStyleSheet("""
            QAbstractItemView {
                padding: 2px 0px;
                selection-background-color: #29bec5;
                selection-color: black;
            }
            QAbstractItemView::item {
                text-align: left; /* Align text to the left (default) */
                padding-left: 20px; /* Add space from the left */
            }
        """)
        # > Add ComboBox to the form  
        objective_function_widget.layout().addWidget(self.max_min_combobox)

        # > Add inputs (QLineWidget) to objective function
        variables_input_array = []
        for i in range(1, self.variables_spinbox.value()+1):
            input = QLineEdit(objective_function_widget)
            input.setValidator(QDoubleValidator(input))
            self.Border_Color_Style(input, "black")


            objective_function_widget.layout().addWidget(input)

            label = QLabel("X<sub>{0}</sub>".format(i))
            label.setStyleSheet("""
                                font-size: 20px;    
                                font-weight: bold;
                                """)
            objective_function_widget.layout().addWidget(label)
            
            if i != self.variables_spinbox.value():
                label = QLabel("+")
                label.setStyleSheet("""
                                    font-size: 20px;
                                    """)
                objective_function_widget.layout().addWidget(label)

            variables_input_array.append(input)

        # > Add objective function widget to the form
        self.form_layout_2.addRow(objective_function_widget)

        # > Contrainte Label and Style
        label = QLabel("Contraints:")
        label.setStyleSheet("font-size: 20px;")
        # > Add Contrainte Label to the Form
        self.form_layout_2.addRow(label) 

        # > All Contraintes Widget 
        constraint_widget = QWidget(self.form_widget_2)
        constraint_widget.setLayout(QVBoxLayout())

        # > Lists to Save inputs
        contraint_input_array = []
        single_contraint_input_array = []
        contraint_input_result_array = []

        # > Add inputs (QLineWidget) to the Contraintes
        for i in range(0, self.constraint_spinbox.value()):
            label = QLabel("Constraint {0}:".format(i+1))
            label.setStyleSheet("font-size: 18px;")
            constraint_widget.layout().addWidget(label)
            
            single_constraint_widget = QWidget(constraint_widget)
            single_constraint_widget.setLayout(QHBoxLayout())

            for j in range(1, self.variables_spinbox.value()+1):
                input = QLineEdit(single_constraint_widget)
                input.setValidator(QDoubleValidator(input))
                self.Border_Color_Style(input, "black")


                single_constraint_widget.layout().addWidget(input)
                
                label = QLabel("X<sub>{0}</sub>".format(j))
                label.setStyleSheet("""
                                    font-size: 20px;    
                                    font-weight: bold;
                                    """)
                single_constraint_widget.layout().addWidget(label)
                
                if j != self.variables_spinbox.value():
                    label = QLabel("+")
                    label.setStyleSheet("font-size: 20px;")
                    single_constraint_widget.layout().addWidget(label)
                else :
                    label = QLabel("<span>&le;</span>")
                    label.setStyleSheet("font-size: 20px;")
                    single_constraint_widget.layout().addWidget(label)

                single_contraint_input_array.append(input)
                pass
            

            input = QLineEdit(single_constraint_widget)
            input.setValidator(QDoubleValidator(input))
            self.Border_Color_Style(input, "black")


            single_constraint_widget.layout().addWidget(input)
            contraint_input_result_array.append(input)

            contraint_input_array.append(single_contraint_input_array.copy())
            single_contraint_input_array.clear()

            constraint_widget.layout().addWidget(single_constraint_widget)

            pass

        # > Add Constraintes Widget to form
        self.form_layout_2.addRow(constraint_widget)

        # > Contrainte de Non-négativité
        contraint_non_negativite = "<b style='font-size: 20px;'>"
        for i in range(self.variables_spinbox.value()):
            contraint_non_negativite += f"X<sub>{i+1}</sub>"
            if i != self.variables_spinbox.value() - 1:
                contraint_non_negativite += ", "
        
        contraint_non_negativite += "<span> &ge; 0</span> </b>"

        # > Non-négativité labels
        label = QLabel(contraint_non_negativite)
        label.setAlignment(Qt.AlignCenter)

        # > Add Non-négativité labels
        self.form_layout_2.addRow(QLabel("<div style='font-size: 20px;'>Contrainte de Non-négativitée :</div>"), label)
        
        # > Add Solve Button to the form
        submit_btn = QPushButton("Générer", clicked = lambda : self.Solve_Simlexe(variables_input_array, contraint_input_array, contraint_input_result_array))
        submit_btn.setStyleSheet("""
                                    QPushButton {
                                        padding: 10px 20px;
                                        margin: 10px;
                                        color: white;
                                        font: 18px bold;
                                        background-color: #29bec5;
                                        border-radius: 5px;
                                        border: 2px solid transparent;
                                    }
                                    QPushButton:hover {
                                        color: #29bec5;
                                        background-color: white;
                                        border: 2px solid #29bec5;
                                    }
                                    QPushButton:pressed {
                                        color: white;
                                        background-color: #29bec5;
                                    }
                                """)
        self.form_layout_2.addRow(submit_btn)

        # > Add the form to the main Widget
        self.main_widget.layout().addWidget(self.form_widget_2)

        return

    def reset(self, values:bool):
        # > Reset the spinboxes to 0
        if values == True:
            self.variables_spinbox.setValue(0)
            self.constraint_spinbox.setValue(0)

        # > Destroy form_widget_2 if it exists
        if self.form_widget_2 != None:
            self.form_widget_2.deleteLater() 
            self.form_widget_2 = None

        # > Destroy All_Tables_widget if it exists
        if self.All_Tables_widget != None:
            self.All_Tables_widget.deleteLater() 
            self.All_Tables_widget = None

        return

    def Solve_Simlexe(self, variables_input_array:list, contraint_input_array:list, contraint_input_result_array:list):

        if self.All_Tables_widget != None:
            self.All_Tables_widget.deleteLater()
            self.All_Tables_widget = None

        # > If one of the inputs is empty return
        if self.Check_Inputs(variables_input_array, contraint_input_array, contraint_input_result_array) == False:
            return
        else:
            self.Return_inputs_to_black(variables_input_array, contraint_input_array, contraint_input_result_array)
    
        # > Identifiez le nombre des variable de decision et de constraint
        variable_nbr = self.variables_spinbox.value()
        contstraint_nbr = self.constraint_spinbox.value()

        # > Initialisez une matrice des valeur des tableaux
        self.table_matrix = [[]]
        self.fill_matrix(variable_nbr, contstraint_nbr, variables_input_array, contraint_input_array, contraint_input_result_array)

        # > Initialisez un dictionaire pour les headers des tableaux
        self.header_dict = {
            "Row": ['Z'],
            "Column": ['Z']
        }
        self.Define_headers(variable_nbr, contstraint_nbr)


        
        self.All_Tables_widget = QWidget(self.main_widget)
        layout = QVBoxLayout()
        self.All_Tables_widget.setLayout(layout)
        layout.setSpacing(20)  # 20 pixels gap

        self.main_widget.layout().addWidget(self.All_Tables_widget)

        self.Standarisation(variables_input_array, contraint_input_array, contraint_input_result_array)
        
        self.All_Tables_widget.layout().addWidget(QLabel("<b style='font-size: 20px;'>&bull; Solution :</b>"))

        i, j, pivot = self.find_Pivot(self.table_matrix)
        if pivot == None:
            label = QLabel("<b style='font-size: 20px;'>&bull; Tableau Intiale :</b>")
            label.setIndent(30)
            self.All_Tables_widget.layout().addWidget(label)
            
            self.draw_Table(variable_nbr, contstraint_nbr, (-1, -1))
            self.No_Solution()
            return
        
        elif self.check_Z_row(self.table_matrix[0]) == True:
            label = QLabel("<b style='font-size: 20px;'>&bull; Tableau Intiale :</b>")
            label.setIndent(30)
            self.All_Tables_widget.layout().addWidget(label)

            self.draw_Table(variable_nbr, contstraint_nbr, (-1, -1))
            self.Table_Description(variable_nbr, contstraint_nbr, -1, -1)
            
            for i in range(self.table_widget.rowCount()):
                for j in range(self.table_widget.columnCount()):

                    a = self.table_widget.item(i, j)
                    if i == 0 and j == self.table_widget.columnCount() -1:
                        a.setBackground(QColor("#91efb6")) # >>
                    
                    pass

                pass     
            
            return

        else:
            label = QLabel("<b style='font-size: 20px;'>&bull; Tableau Intiale :</b>")
            label.setIndent(30)
            self.All_Tables_widget.layout().addWidget(label)

            self.draw_Table(variable_nbr, contstraint_nbr, (i, j))
            self.Table_Description(variable_nbr, contstraint_nbr, i, j)
            self.transform_matrix((i, j, pivot))


        conteur = 1

        while self.check_Z_row(self.table_matrix[0]) == False and pivot != None:

            self.header_dict["Column"][i] = self.header_dict["Row"][j]
            
            i, j, pivot = self.find_Pivot(self.table_matrix)

            if pivot == None:
                label = QLabel(f"<b style='font-size: 20px;'>&bull; Iteration {conteur} :</b>")
                label.setIndent(30)
                self.All_Tables_widget.layout().addWidget(label)

                self.draw_Table(variable_nbr, contstraint_nbr, (-1, -1))
                self.No_Solution()
            else:
                label = QLabel(f"<b style='font-size: 20px;'>&bull; Iteration {conteur} :</b>")
                label.setIndent(30)
                self.All_Tables_widget.layout().addWidget(label)

                self.draw_Table(variable_nbr, contstraint_nbr, (i, j))
                self.Table_Description(variable_nbr, contstraint_nbr, i, j)
                self.transform_matrix((i, j, pivot))

            conteur += 1


        if pivot != None:
            label = QLabel(f"<b style='font-size: 20px;'>&bull; Iteration {conteur} :</b>")
            label.setIndent(30)
            self.All_Tables_widget.layout().addWidget(label)

            self.header_dict["Column"][i] = self.header_dict["Row"][j]
            self.draw_Table(variable_nbr, contstraint_nbr, (-1, -1))
            self.Table_Description(variable_nbr, contstraint_nbr, i, j)

            for i in range(self.table_widget.rowCount()):
                for j in range(self.table_widget.columnCount()):

                    a = self.table_widget.item(i, j)
                    if i == 0 and j == self.table_widget.columnCount() -1:
                        a.setBackground(QColor("#91efb6")) # >>
                    
                    pass

                pass     

        
        return

    def Standarisation(self, variables_input_array:list, contraint_input_array:list, contraint_input_result_array:list):
        
        label = QLabel("<b style='font-size: 20px;'>&bull; Standarisation du Probléme :</b>")
        self.All_Tables_widget.layout().addWidget(label)


        stadarisation_widget = QWidget()
        layout = QVBoxLayout()
        stadarisation_widget.setLayout(layout)

        stadarisation_widget.setFixedWidth(900)

        # > Add an object name to the paragraph so that the styling doesn't effect the children widgets
        stadarisation_widget.setObjectName("standarisation_widget")

        # > Style the description paragraph
        stadarisation_widget.setStyleSheet("""
                                            #standarisation_widget {
                                                background-color: white;  
                                                border: 1px solid #ccc;
                                                border-radius: 5px;
                                            }
                                        """)

        # > Add a shadow effect
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(15)
        shadow_effect.setOffset(0, 0)
        shadow_effect.setColor(QColor(0, 0, 0, 160))

        # > Add the graphics of the shadow effect
        stadarisation_widget.setGraphicsEffect(shadow_effect)

        # > Create objective function string
        objective_function = "<div style='font-size: 20px;padding-left: 20px;'>max Z = "
        for i, x in enumerate(variables_input_array):
            if self.max_min_combobox.currentText() == "Minimiser":
                if -1*float(x.text()) < 0 and i != 0:
                    objective_function = objective_function[0:-2] + '- '
                    fraction = Fraction(float(x.text())).limit_denominator()
                else:
                    fraction = Fraction(-1*float(x.text())).limit_denominator()
                objective_function += str(fraction) + f' X<sub>{i+1}</sub>'

            else :
                if float(x.text()) < 0 and i != 0:
                    objective_function = objective_function[0:-2] + '- '
                    fraction = Fraction(-1*float(x.text())).limit_denominator()
                else:
                    fraction = Fraction(float(x.text())).limit_denominator()
                objective_function += str(fraction) + f' X<sub>{i+1}</sub>'
            objective_function += " + "

        for i, x in enumerate(contraint_input_array):
            objective_function += "0" + f' S<sub>{i+1}</sub>'

            if i != len(contraint_input_array) - 1:
                objective_function += " + "

        objective_function += "</div>"

        # > objective function Qwidget
        objective_function_widget = QWidget()
        layout = QVBoxLayout()
        objective_function_widget.setLayout(layout)

        # > Create and add objective function Label to the objective function Qwidget
        objective_function_label = QLabel(objective_function)
        objective_function_label.setIndent(50)
        objective_function_widget.layout().addWidget(objective_function_label)

        # > check is the problem is min 
        if self.max_min_combobox.currentText() == "Minimiser":
            stadarisation_widget.layout().addWidget(QLabel("<b style='font-size: 20px;'><u>Probléme de Minimisation :</u></b>"))
            label = QLabel("<div style='font-size: 20px;'>min Z = c X  &hArr; - max Z = - c X</div>")
            label.setIndent(70)
            stadarisation_widget.layout().addWidget(label)

        stadarisation_widget.layout().addWidget(QLabel("<b style='font-size: 20px;'><u>Fonction objectif :</u></b>"))
        stadarisation_widget.layout().addWidget(objective_function_widget)
        stadarisation_widget.layout().addWidget(QLabel("<b style='font-size: 20px;'><u>Sous Contraint :</u></b>"))

        contraint_widget = QWidget()
        layout = QVBoxLayout()
        contraint_widget.setLayout(layout)

        for i in range(self.constraint_spinbox.value()):
            constraint = "<span style='font-size: 20px;'>\t"
            for j, x in enumerate(contraint_input_array[i]):
                if float(x.text()) < 0 and j != 0:
                    constraint = constraint[0:-2] + '- '
                    fraction = Fraction(-1*float(x.text())).limit_denominator()
                else:
                    fraction = Fraction(float(x.text())).limit_denominator()
                constraint += str(fraction) + f' X<sub>{i+1}</sub>'
                constraint += " + "

            for k, x in enumerate(contraint_input_array):
                if k != i:
                    constraint += "0" + f' S<sub>{k+1}</sub>'
                else:
                    constraint += "1" + f' S<sub>{k+1}</sub>'

                if k != len(contraint_input_array[i]) - 1:
                    constraint += " + "

            fraction = Fraction(float(contraint_input_result_array[i].text())).limit_denominator()
            constraint += " = " + f"{str(fraction)}"
            constraint += "</span>"

            label = QLabel(constraint)
            label.setIndent(50)
            contraint_widget.layout().addWidget(label)

        stadarisation_widget.layout().addWidget(contraint_widget)
        
            
        # > Add Non-négativité labels
        stadarisation_widget.layout().addWidget(QLabel("<b style='font-size: 20px;'><u>Contrainte de Non-négativitée :</u></b>"))

        # > Contrainte de Non-négativité
        contraint_non_negativite = "<div style='font-size: 20px;'>"
        for i in range(self.variables_spinbox.value()):
            contraint_non_negativite += f"X<sub>{i+1}</sub>"
            contraint_non_negativite += ", "
        
        for i in range(self.constraint_spinbox.value()):
            contraint_non_negativite += f"S<sub>{i+1}</sub>"
            if i != self.constraint_spinbox.value() - 1:
                contraint_non_negativite += ", "
        
        contraint_non_negativite += "<span> &ge; 0</span> </div>"
            
        # > Non-négativité labels
        label = QLabel(contraint_non_negativite)
        label.setIndent(70)

        # > Add Non-négativité labels
        stadarisation_widget.layout().addWidget(label)

        self.All_Tables_widget.layout().addWidget(stadarisation_widget)
        self.All_Tables_widget.layout().setAlignment(stadarisation_widget, Qt.AlignCenter)


        return

    def draw_Table(self, V_number:int, C_number:int, Pivot:tuple):

        self.table_widget = QTableWidget(self.main_widget)
        self.table_widget.setRowCount(1 + C_number)  # Set number of rows
        self.table_widget.setColumnCount(1 + V_number + C_number + 1)  # Set number of columns
        self.table_widget.setHorizontalHeaderLabels(self.header_dict["Row"])
        self.table_widget.setVerticalHeaderLabels(self.header_dict["Column"])

        # > Disable selecting for the entire table:
        self.table_widget.setSelectionMode(QTableWidget.NoSelection)
        # > Disable editing for the entire table:
        self.table_widget.setEditTriggers(QTableWidget.NoEditTriggers)

        self.table_widget.setStyleSheet("""
            QHeaderView::section {
                background-color: #29bec5;
                color: black;
                font-weight: bold;
            }
            QTableWidget {
                height: 300px;
            }
        """)

        for i in range(self.table_widget.rowCount()):
            self.table_widget.setRowHeight(i, 50)

        for j in range(self.table_widget.columnCount()):
            self.table_widget.setColumnWidth(j, 150)

        # > Set font size of headers:
        header_font = QFont()
        header_font.setPointSize(15)
        self.table_widget.horizontalHeader().setFont(header_font)
        self.table_widget.verticalHeader().setFont(header_font)

        # > Set font size of elements:
        font = self.table_widget.font()
        font.setPointSize(15)
        self.table_widget.setFont(font)

        self.table_widget.setFixedWidth(self.table_widget.columnWidth(1) * (1 + V_number + C_number + 1) + self.table_widget.verticalHeader().width() + 3)
        self.table_widget.setFixedHeight(self.table_widget.rowHeight(1) * (1 + C_number) + self.table_widget.horizontalHeader().height() + 2)        

        for row, rowData in enumerate(self.table_matrix):
            for column, value in enumerate(rowData):
                fraction = Fraction(value).limit_denominator()
                item = QTableWidgetItem(str(fraction))

                item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

                if row == Pivot[0] and column == Pivot[1]:
                    item.setBackground(QColor("#FCA746"))

                self.table_widget.setItem(row, column, item)

        self.All_Tables_widget.layout().addWidget(self.table_widget)
        self.All_Tables_widget.layout().setAlignment(self.table_widget, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        return

    def Table_Description(self, V_number:int, C_number:int, row:int, column:int):

        # > Define the description paragraph with a vertical box layout
        description_widget = QWidget(self.All_Tables_widget)
        layout = QVBoxLayout()
        description_widget.setLayout(layout)
        description_widget.setFixedWidth(900)

        # > Add the description paragraph of the table to the parent widget
        self.All_Tables_widget.layout().addWidget(description_widget)

        # > Align description paragraph in the middle
        self.All_Tables_widget.layout().setAlignment(description_widget, Qt.AlignCenter)

        # > Add a shadow effect
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(15)
        shadow_effect.setOffset(0, 0)
        shadow_effect.setColor(QColor(0, 0, 0, 160))

        # > Add the graphics of the shadow effect
        description_widget.setGraphicsEffect(shadow_effect)
        
        # > Extreme Point and Base Qwidget with a Horizontal box Layout
        label_wigdet = QWidget(description_widget)
        layout = QHBoxLayout()
        label_wigdet.setLayout(layout)

        # > Find Extreme Point 
        ptn_extreme = self.find_Point_extreme(V_number, C_number)

        # > Extreme Point QLabel and style and Center Align 
        label = QLabel(f"<b style='color: black;'>&bull; Point Extreme :</b> {ptn_extreme}", parent=label_wigdet)
        label.setStyleSheet("""
                                    font-size: 20px;
                                    color: gray;
                            """)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # > Add Extreme Point QLabel to the QWidget 
        label_wigdet.layout().addWidget(label)

        # > Find Base
        base = self.find_Base(C_number)

        # > Base QLabel and style and Center Align 
        label = QLabel(f"<b style='color: black;'>&bull; Base :</b> {base}", parent=label_wigdet)
        label.setStyleSheet("""
                                    font-size: 20px;
                                    color: gray;
                            """)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # > Add Base QLabel to the QWidget 
        label_wigdet.layout().addWidget(label)

        # > Add QWidget to the description paragraph 
        description_widget.layout().addWidget(label_wigdet)


        # > Optimality Test 
        if self.check_Z_row(self.table_matrix[0]) == True:
            self.Solution(description_widget)
            return
                

        # > Optimality Test QLabel and style 
        label = QLabel(f"<b style='color: black;'>&bull; Test d'Optimalité :</b> la base ne correspond pas à une solution optimale car: <b style='color: black;'>Z<sub>{column}</sub> - C<sub>{column}</sub> &lt; 0</b>", parent=description_widget)
        label.setStyleSheet("""
                                    font-size: 20px;
                                    color: gray;
                            """)

        # > Add Optimality Test QLabel to the description paragraph
        description_widget.layout().addWidget(label)


        # > First Criteria of Dantzig QLabel and its style
        label = QLabel(f"<b style='color: black;'>&bull; Premier critére de Dentzig : {self.header_dict["Row"][column][0]}<sub>{self.header_dict["Row"][column][1]}</sub></b> doit entrer dans la base.", parent=description_widget)
        label.setStyleSheet("""
                                    font-size: 20px;
                                    color: gray;
                            """)

        # > Add the First Criteria of Dantzig QLabel to the description paragraph
        description_widget.layout().addWidget(label)

        # > Second Criteria of Dantzig QLabel and its style
        label = QLabel(f"<b style='color: black;'>&bull; Deuxieme critére de Dentzig : {self.header_dict["Column"][row][0]}<sub>{self.header_dict["Row"][row][1]}</sub></b> doit sortir de la base.", parent=description_widget)
        label.setStyleSheet("""
                                    font-size: 20px;
                                    color: gray;
                            """)

        # > Add an object name to the paragraph so that the styling doesn't effect the children widgets
        description_widget.setObjectName("description_widget")

        # > Style the description paragraph
        description_widget.setStyleSheet("""
                                            #description_widget {
                                                background-color: #fcf3b8;  
                                                border: 1px solid #ccc;
                                                border-radius: 5px;
                                            }
                                        """)

        # > Add the Second Criteria of Dantzig QLabel to the description paragraph
        description_widget.layout().addWidget(label)

        return

    def Border_Color_Style(self, input:QLineEdit,color:str):

        # > Set a Styling on the inputs with the color black as the border color
        if color == "black":
            input.setStyleSheet("""
                            QLineEdit {
                                font-size: 20px;
                                height: 40px;
                                border-radius: 5px;
                                border: 2px solid #3d3e3f;
                            }
                            QLineEdit:focus {
                                border-color: #29bec5;
                            }
                            """)
            
        # > Set a Styling on the inputs with the color red as the border color
        elif color == "red":
            input.setStyleSheet("""
                            QLineEdit {
                                font-size: 20px;
                                height: 40px;
                                border-radius: 5px;
                                border: 2px solid #ff6c22;
                            }
                            QLineEdit:focus {
                                border-color: #29bec5;
                            }
                            """)

        return
  
    def Return_inputs_to_black(self, variables_input_array:list, contraint_input_array:list, contraint_input_result_array:list):
        
        # > Return the color of all the inputs to black

        for x in variables_input_array:
            self.Border_Color_Style(x, "black")

        for x in contraint_input_array:
            for y in x:
                self.Border_Color_Style(y, "black")

        for x in contraint_input_result_array:
            self.Border_Color_Style(x, "black")

        return

    def Check_Inputs(self, variables_input_array:list, contraint_input_array:list, contraint_input_result_array:list):

        Answer = True

        for x in variables_input_array:
            if x.text() == "":
                Answer = False
                self.Border_Color_Style(x, "red")

        for x in contraint_input_array:
            for y in x:
                if y.text() == "":
                    Answer = False
                    self.Border_Color_Style(y, "red")

        for x in contraint_input_result_array:
            if x.text() == "":
                Answer = False
                self.Border_Color_Style(x, "red")

        return Answer

    def No_Solution(self):
        min = 0
        index = 0
        for i, x in enumerate(self.table_matrix[0]):
            if x < min:
                min = x
                index = i

        description_widget = QWidget(self.All_Tables_widget)
        layout = QVBoxLayout()
        description_widget.setLayout(layout)

        description_widget.setFixedWidth(900)

        # > Add an object name to the paragraph so that the styling doesn't effect the children widgets
        description_widget.setObjectName("description_widget")

        # > Style the description paragraph
        description_widget.setStyleSheet("""
                                            #description_widget {
                                                background-color: #ffbcbc;
                                         
                                                border-radius: 5px;
                                            }
                                        """)
        # > Add the description paragraph of the table to the parent widget
        self.All_Tables_widget.layout().addWidget(description_widget)

        # > Align description paragraph in the middle
        self.All_Tables_widget.layout().setAlignment(description_widget, Qt.AlignmentFlag.AlignCenter)

        # > Add a shadow effect
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(15)
        shadow_effect.setOffset(0, 0)
        shadow_effect.setColor(QColor(0, 0, 0, 160))

        # > Add the graphics of the shadow effect
        description_widget.setGraphicsEffect(shadow_effect)


        label1 = QLabel(f"<b style='color: black;'>&bull; {self.header_dict["Row"][index]}</b> doit entrer dans la base et aucun variable peut sortir. ")
        label1.setStyleSheet("""
                                    font-size: 20px;
                                    color: gray;
                            """)
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label2 = QLabel(f"Donc ce probleme n'admet <b style='color: black;'>aucun Solution.</b>")
        label2.setStyleSheet("""
                                    font-size: 20px;
                                    color: gray;
                            """)
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
        description_widget.layout().addWidget(label1)
        description_widget.layout().addWidget(label2)
        return

    def Solution(self, description_widget:QWidget):
        res = self.test_Infinity_of_solutions()

        # > Add an object name to the paragraph so that the styling doesn't effect the children widgets
        description_widget.setObjectName("description_widget")

        # > Style the description paragraph
        description_widget.setStyleSheet("""
                                            #description_widget {
                                                background-color: #91efb6;  
                                                border: 1px solid #ccc;
                                                border-radius: 5px;
                                            }
                                        """)

        if res == None:   ## > Solution unique


            result = self.find_Result()
            label1 = QLabel(f"<b style='color: black;'>&bull; Test d'Optimalité :</b> la base correspond à une solution optimale car: <b style='color: black;'>Z<sub>j</sub><sup>N</sup> - C<sub>j</sub><sup>N</sup> &gt; 0</b> ")
            label1.setStyleSheet("""
                                        font-size: 20px;
                                        color: gray;
                                """)
            
            if self.max_min_combobox.currentText() == "Minimiser":
                solution = f"min Z = {str(Fraction(-1*self.table_matrix[0][-1]).limit_denominator())}"
            else:
                solution = f"max Z = {str(Fraction(self.table_matrix[0][-1]).limit_denominator())}"

            label2 = QLabel(f"Donc la <b style='color: black;'>Solution est Unique </b> <b style='color: green;'>{result}, {solution}</b>")
            label2.setStyleSheet("""
                                        font-size: 20px;
                                        color: gray;
                                """)
            label3 = None
    
        else :   ## > infinité de solution
            
            result = self.find_Result()
            label1 = QLabel(f"<b style='color: black;'>&bull; Test d'Optimalité :</b> la base correspond à une solution optimale car: <b style='color: black;'>Z<sub>j</sub> - C<sub>j</sub> &ge; 0,</b> ")
            label1.setStyleSheet("""
                                        font-size: 20px;
                                        color: gray;
                                """)
    
            label2 = QLabel(f"Donc il y a une <b style='color: black;'>Infinité de Solutions</b> car: <b style='color: black;'>Z<sub>{res}</sub> - C<sub>{res}</sub> = 0,</b> ")
            label2.setStyleSheet("""
                                        font-size: 20px;
                                        color: gray;
                                """)

            if self.max_min_combobox.currentText() == "Minimiser":
                solution = f"min Z = {str(Fraction(-1*self.table_matrix[0][-1]).limit_denominator())}"
            else:
                solution = f"max Z = {str(Fraction(self.table_matrix[0][-1]).limit_denominator())}"

            label3 = QLabel(f"parmi les solution on trouve : <b style='color: green;'>{result}, {solution}</b>")
            label3.setStyleSheet("""
                                        font-size: 20px;
                                        color: gray;
                                """)

        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        description_widget.layout().addWidget(label1)
        description_widget.layout().addWidget(label2)

        if label3 != None:
            label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
            description_widget.layout().addWidget(label3)

        return
    
# ******************************** Le Code ***************************************** #
    # > initialiser les headers (ligne, colonne) de tableau initial
    def Define_headers(self, variable_nbr:int, contstraint_nbr:int):

        # > Remplir le header des colonne
        for i in range(1, variable_nbr + contstraint_nbr + 1):
            if i <= variable_nbr:
                self.header_dict["Row"].append(f"X{i}")
            else :
                self.header_dict["Row"].append(f"S{i-variable_nbr}")
            pass

        self.header_dict["Row"].append("bi")

        # > Remplir le header des colonne
        for i in range(1, contstraint_nbr+1):
            self.header_dict["Column"].append(f'S{i}')
            pass

        return

    # > Remplir la matrice "table_matrix" par les coefficient de probleme
    def fill_matrix(self, variable_nbr:int, contstraint_nbr:int, variables_input_array:list, contraint_input_array:list, contraint_input_result_array:list):

        # > Initialiser les lignes de la matrice
        for i in range(1, contstraint_nbr+1):
            self.table_matrix.append([])
            pass

        # > Remplir la matrice
        for i, x in enumerate(self.table_matrix):
            if i == 0:
                x.append(1)
                for y in variables_input_array:
                    if self.max_min_combobox.currentText() == "Maximiser":
                        try:
                            x.append(-1*int(y.text()))
                        except:
                            x.append(-1*float(y.text()))
                    elif self.max_min_combobox.currentText() == "Minimiser":
                        try:
                            x.append(int(y.text()))
                        except:
                            x.append(float(y.text()))

                for y in range(contstraint_nbr):
                    x.append(0)
                
                x.append(0)
            
            else:

                x.append(0)
                for y in contraint_input_array[i-1]:
                    try:
                        x.append(int(y.text()))
                    except:
                        x.append(float(y.text()))

                for y in range(contstraint_nbr):
                    x.append(0)

                try:
                    x.append(int(contraint_input_result_array[i-1].text()))
                except:
                    x.append(float(contraint_input_result_array[i-1].text()))
            pass
        
        # > Remlir les valeur des variables de decart par 1 pour chaque contrait 
        for i in range(0, contstraint_nbr):
            for j in range(0, contstraint_nbr):
                if i == j:
                    self.table_matrix[i+1][1 + variable_nbr + j] = 1
                pass
            
        return

    # > Trouver le resultat finale de probleme et retourne une chaine de caractére Exemple (X1=0, X2=2)
    def find_Result(self):

        Result = ""

        for i in range(1, self.variables_spinbox.value()+1):
            Result += f"X<sub>{i}</sub> = "
            x = ""
            for j, x in enumerate(self.header_dict["Column"][1:]):
                if x == f"X{i}":
                    fraction = Fraction(self.table_matrix[j+1][-1]).limit_denominator()
                    Result += f"{str(fraction)}"
                    break
            if x != f"X{i}":
                Result += "0"
            if i != self.variables_spinbox.value():
                Result += ", "

                pass

        return Result

    # > Retourner le point extreme de tableux Exemple (0, 0, 2, 1)
    def find_Point_extreme(self, V_number:int, C_number:int):

        ptn_extreme = "("            

        # > Add the decision variables (X1, X2...) to the extreme point
        for i in range(V_number):
            nbr = 0
            for j in range(1, len(self.header_dict["Column"])):
                if f"X{i+1}" == self.header_dict["Column"][j]:
                    if int(self.table_matrix[j][-1]) == float(self.table_matrix[j][-1]):
                        nbr = int(self.table_matrix[j][-1])
                    else:
                        nbr = self.table_matrix[j][-1]
                    break
            fraction = Fraction(nbr).limit_denominator()
            ptn_extreme += f"{str(fraction)}, "
            pass

        # > Add the decart variables (S1, S2...) to the extreme point
        for i in range(C_number):
            nbr = 0
            for j in range(1, len(self.header_dict["Column"])):
                if f"S{i+1}" == self.header_dict["Column"][j]:
                    if int(self.table_matrix[j][-1]) == float(self.table_matrix[j][-1]):
                        nbr = int(self.table_matrix[j][-1])
                    else:
                        nbr = self.table_matrix[j][-1]
                    break
            
            fraction = Fraction(nbr).limit_denominator()
        
            if i != C_number-1:
                ptn_extreme += f"{str(fraction)}, "
            else:
                ptn_extreme += f"{str(fraction)})"
            pass

        return ptn_extreme

    # > Retourner la base de tableux Exemple (S1, X1)
    def find_Base(self, C_number:int):

        base = "("
        
        for i in range(1, C_number+1):
            if i == C_number:
                base += f"{self.header_dict["Column"][i][0]}<sub>{self.header_dict["Column"][i][1]}</sub>)"
            else:
                base += f"{self.header_dict["Column"][i][0]}<sub>{self.header_dict["Column"][i][1]}</sub>, "
            pass

        return base

    # > Trouver le pivot et retourner leur indice dans la matrice s'il existe Exemple (i=1, j=2)
    # > sinon il retourne (None, None)
    def find_Pivot(self, matrix:list):

        Pivot = None

        # > Search the min in the Z row
        Z_row = matrix[0]
        min = Z_row[0]
        min_index = 0
        for i in range(len(Z_row)):
            if Z_row[i] < min:
                min = Z_row[i]
                min_index = i
        
        # > Array of possible Value for pivot
        array = []
        for i in range(1, len(matrix)) :
            if matrix[i][min_index] <= 0:
                array.append(None)
            else:
                array.append(matrix[i][-1] / matrix[i][min_index])
            pass

        # > Search the min value in the array
        min = array[0]
        min_y_index = 1
        for i in range(len(array)):
            if min == None:
                min = array[i]
                min_y_index = i+1
            elif array[i] == None:
                continue
            elif array[i] < min:
                min = array[i]
                min_y_index = i+1

        # > Return the Pivot or if there is none return None 
        if min == None:
            return None, None, None
        else:
            Pivot = matrix[min_y_index][min_index]
            return min_y_index, min_index, Pivot
        
        return

    # > Tester la condition d'arret si la ligne de Z est superieur à 0 (Zi-Ci>=0) et retourne True si
    # > c'est le cas sinon retourne False
    def check_Z_row(self, row:list):
        # > Check if the values of the Z row are positive
        for x in row[:-1]:
            if x < 0:
                return False
        
        return True

    # > Calculer et modifier les elements de la matrice en utilisant la methode de carré
    def transform_matrix(self, Pivot:tuple):
        self.table_matrix

        # > Evaluate the matrix with the Rectangle Methode
        for i, x in enumerate(self.table_matrix):
            if i == Pivot[0]:
                continue
            for j in range(len(x)):
                if j == 0 or j == Pivot[1]:
                    continue

                if j < Pivot[1]:
                    if i < Pivot[0]:
                        self.table_matrix[i][j] -= (self.table_matrix[i][Pivot[1]] * self.table_matrix[Pivot[0]][j]) / Pivot[2] 
                
                    elif i > Pivot[0]:
                        self.table_matrix[i][j] -= (self.table_matrix[i][Pivot[1]] * self.table_matrix[Pivot[0]][j]) / Pivot[2] 
                
                elif j > Pivot[1]:
                    if i < Pivot[0]:
                        self.table_matrix[i][j] -= (self.table_matrix[i][Pivot[1]] * self.table_matrix[Pivot[0]][j]) / Pivot[2] 
                
                    elif i > Pivot[0]:
                        self.table_matrix[i][j] -= (self.table_matrix[i][Pivot[1]] * self.table_matrix[Pivot[0]][j]) / Pivot[2] 

        # > Return the values of Column of the Pivot to 0 
        for i, x in enumerate(self.table_matrix):
            if i != Pivot[0]:
                x[Pivot[1]] = 0 
            pass

        # > Devise the Row of the Pivot on the Pivot
        for i in range(len(self.table_matrix[Pivot[0]])):
            if i != 0:
                self.table_matrix[Pivot[0]][i] /= Pivot[2] 
            pass

        return

    # > Tester s'il existe une infinité de solution , si Zi-Ci = 0 et retourne i qui est l'indice de Zi-Ci
    # > si c'est vrai, sinon retoune None
    def test_Infinity_of_solutions(self):
        
        for i, x in enumerate(self.header_dict["Row"][1:-1]):
            if self.table_matrix[0][i+1] == 0:
                find = False
                for j, y in enumerate(self.header_dict["Column"][1:]):
                    if x == y:
                        find = True
                        break
                
                if find == False:
                    return i+1
                
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Simplexe()
    window.show()
    sys.exit(app.exec_())

# * Commande pour transformer le code vers un programme (.py => .exe)
# > pyinstaller --onefile --windowed --icon=images\\Simplexe.ico main.py --name "Simplexe"