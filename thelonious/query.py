from database import Thelonious

if __name__ == "__main__":
    theDB = Thelonious()

    shohin = theDB.Table.create("shohin", {"shohin_id", "shohin_name", "kubun_id", "price"})

    shohin = shohin.insert(1, "りんご", 1, 300)
    shohin = shohin.insert(2, "みかん", 1, 130)
    shohin = shohin.insert(3, "キャベツ", 2, 200)
    shohin = shohin.insert(4, "わかめ", 2, 200)

    print(shohin.columns)
    print(shohin.columns[0].name)

    print(shohin.taples)
    print(shohin.taples[0].values)

    #print(shohin.columns[0])
