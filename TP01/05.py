def show_price_to_pay(price: int):
    print(f"Le prix a payer est : {price}")


# prix d'un ticket de base
ticket_price: int = 10
# Si l'utilisateur à une carte mensuelle le prix du billet est gratuit
has_monthly_card: str = input("Possédez-vous la carte mensuelle ? (oui ou non) ")
if has_monthly_card.lower() == "oui":
    show_price_to_pay(0)
else:
    has_half_price: str = input("Possédez-vous le demi-tarif ? (oui ou non) ")
    has_student_discount: str = input("Possédez-vous la carte étudiante ? (oui ou non) ")
    # si l'utilisateur n'a pas de rabais il peut choisir le nombre de billet et beneficier d'un rabais à partir de 4 billets
    if not (has_half_price or has_student_discount):
        no_ticket_wanted: int = int(input("Combien de billets voulez-vous ? "))
        show_price_to_pay(no_ticket_wanted * ticket_price if no_ticket_wanted < 4 else no_ticket_wanted * (ticket_price - 2))
    # si l'utilisateur à un rabais il prendra un billet et on lui applique les rabais avant d'afficher le prix
    else:
        ticket_value: int = ticket_price
        if has_half_price.lower() == "oui":
            ticket_value -= 5
        if has_student_discount.lower() == "oui":
            ticket_value -= 2
        show_price_to_pay(ticket_value)
