from pymining import itemmining, assocrules
import MySQLdb
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--username", help="type the username used to access the database", default="root")

    parser.add_argument("--password", help="type your password", default="tommaso")

    parser.add_argument("--name", help="type the database name", default="tracks")

    parser.add_argument("--filename", help="choose the file where you want to save Data Analysis results ",
                        default="analysis.txt")

    parser.add_argument("--minimum_support", type=int,
                        help="chose the minimun support for the association rules algorithm", default=15)

    args = parser.parse_args()

    db = MySQLdb.connect("localhost", "root", "tommaso", "tracks")

    cursor = db.cursor()

    sql1 = "SELECT `progressivoSDO` FROM `tracks`.`interventoPrincipale`;"

    cursor.execute(sql1)

    data1 = cursor.fetchall()

    array1 = []

    for row in data1:
        array1.append(row[0])

    sql2 = """SELECT interventoPrincipale.interventoPrincipale, interventiSecondari.interventiSecondari,
    interventoPrincipale.progressivoSDO
    FROM interventoPrincipale
    INNER JOIN interventiSecondari
    ON interventoPrincipale.progressivoSDO=interventiSecondari.progressivoSDO"""

    cursor.execute(sql2)

    data2 = cursor.fetchall()

    array2 = []

    for sdo in array1:
        temp = []
        counter = 0
        for op in data2:
            if op[2] == sdo:
                if counter == 0:
                    temp.append(op[0])
                temp.append(op[1])
                counter += 1
        array2.append(temp)



    input = itemmining.get_relim_input(array2)

    reportFP = itemmining.relim(input, min_support=args.minimum_support)

    with open("MiningResult.txt", "w") as file:

        file.write("""Frequent ItemSets (DRG codes sets) Mining results: \n""")
        file.write("""\n""")
        file.write("""Note that due to library source code the results are displayed with the following schema: \n""")
        file.write("""       frozenset(DRG codes sets) (support of this sets) \n """)
        file.write("""\n""")

        for rep1 in reportFP:
            print(rep1, reportFP[rep1])
            file.writelines(str(rep1)+str(reportFP[rep1])+"\n")

        reportAR = assocrules.mine_assoc_rules(reportFP, min_support=args.minimum_support, min_confidence=0.5)

        file.write("\n")
        file.write("\n")
        file.write("\n")

        file.write("""Association Rules ItemSets (DRG codes sets) Mining results: \n""")
        file.write("""\n""")
        file.write("""Note that due to library source code the results are displayed with the following schema: \n""")
        file.write("""(frozenset(DRG codes sets 1), frozenset(DRG codes sets 2) where available, (support of this sets), (confidence of this sets) \n """)
        file.write("""\n""")

        for rep2 in reportAR:
            print(rep2)
            file.write(str(rep2)+"\n")
