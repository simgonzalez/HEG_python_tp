def main():
    jours_semaine: list[str] = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    temperatures: list[int] = []
    for day in range(7):
        temperatures.append(int(input(f"Température du jour {jours_semaine[day]} : ")))

    print("\nBILAN DE LA SEMAINE :")
    min_temp: int = 9999
    max_temp: int = -1000
    avg_temp: float = sum(temperatures) / len(temperatures)
    for temp in temperatures:
        if temp < min_temp:
            min_temp = temp
        if temp > max_temp:
            max_temp = temp
    print(f"La température max est {max_temp}")
    print(f"La température min est {min_temp}")
    print(f"La température moyenne est de {avg_temp:.2f}")


if __name__ == "__main__":
    main()
