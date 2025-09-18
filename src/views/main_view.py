"""
Main view - Central menu for the store management application
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from views.user_view import UserView
from views.product_view import ProductView


class MainView:

    @staticmethod
    def show_options():
        """ Show main menu with operation options for users and products """
        while True:
            print("\n===== MENU PRINCIPAL =====\n"
                  "1. Gestion des utilisateurs\n"
                  "2. Gestion des produits\n"
                  "3. Quitter l'application")
            choice = input("Choisissez une option: ")

            if choice == '1':
                print("\n===== GESTION DES UTILISATEURS =====")
                UserView.show_options()
            elif choice == '2':
                print("\n===== GESTION DES PRODUITS =====")
                ProductView.show_options()
            elif choice == '3':
                print("Au revoir!")
                break
            else:
                print("Cette option n'existe pas.")
