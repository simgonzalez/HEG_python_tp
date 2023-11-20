def main():
    random_item_list: list = ["bois", "banc", "bois", "bois"]
    for i in range(random_item_list.count("bois")):
        random_item_list.remove("bois")
    print(*random_item_list)

if __name__ == "__main__":
        main()
