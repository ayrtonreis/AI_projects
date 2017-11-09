import GameManager_3
import time

def main2():
    results = []
    f = open("statistics.txt", "w")  # opens file with name of "test.txt"

    for i in range(10):
        results.append(GameManager_3.play())

        scores = " ".join(str(x) for x in results)
        f.write(scores)
        f.write("\n\n")
        avg = sum(results)/len(results)
    f.write("Average: ")
    f.write(avg)

    print("Results:")
    for score in results:
        print(score)
    print("Average: ", avg)

    f.close()
    time.sleep(999999)

def main():

    f = open("optimization.txt", "w")  # opens file with name of "test.txt"

    parameters = [1, 16, 16]
    max_avg = 0

    for c0 in range(0, 10, 1):
        for c1 in range(1, 1000, 100):
            for c2 in range(1, 1000, 100):
                results = []
                parameters = [c0/10, c1, c2]
                f.write("\nParameters: ")
                string_parameters = " ".join(str(x) for x in parameters)
                f.write(string_parameters)
                f.write("\n")

                for i in range(8):
                    results.append(GameManager_3.play(parameters))
                f.write("Scores: ")
                scores = " ".join(str(x) for x in results)
                f.write(scores)
                f.write("\n\n")

                avg = sum(results)/len(results)
                max_avg = max(max_avg, avg)
                f.write("Average: ")
                f.write(str(avg)+"\n___________________________________")

                print("Results:")
                for score in results:
                    print(score)
                print("Average: ", avg)

    print("Max avg: ", max_avg)
    f.write("\n\nMax avg = "+str(max_avg))
    f.close()
    time.sleep(999999)

if __name__ == '__main__':
    main()