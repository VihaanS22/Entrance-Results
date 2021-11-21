import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

print("")
print("Entrance Results")
print("")
print("Please choose what results you want to see:-")
print("")
print("MATH SCORE")
print("READING SCORE")
print("WRITING SCORE")
print("")

score = input("Please enter your choice all in small letters :- ")

if(score == "reading score"):

    df = pd.read_csv("performance.csv")
    data = df["reading score"].tolist()



    mean = sum(data)/len(data)
    stdev = statistics.stdev(data)
    median = statistics.stdev(data)
    mode = statistics.stdev(data)



    first_start, first_end = mean - stdev, mean + stdev
    sec_start, sec_end = mean - 2*stdev, mean + 2*stdev
    three_start, three_end = mean - 3*stdev, mean + 3*stdev

    listOfFirst = [result for result in data if result>first_start and result<first_end]

    listOf2 = [result for result in data if result>sec_start and result<sec_end]

    listOf3 = [result for result in data if result>three_start and result<three_end]

    print("{} % of data lies between 1 standard deviation and the mean ".format( len(listOfFirst) * 100.0/ len(data) ) )

    print("{} % of data lies between 2 standard deviation and the mean ".format( len(listOf2) * 100.0/ len(data) ) )

    print("{} % of data lies between 3 standard deviation and the mean ".format( len(listOf3) * 100.0/ len(data) ) )


    fig = ff.create_distplot([data], ["reading scores"], show_hist = False)

    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.18], mode = "lines", name = "Mean"))

    fig.add_trace(go.Scatter(x = [first_start, first_start], y = [0, 0.18], mode = "lines", name = "-Deviate"))

    fig.add_trace(go.Scatter(x = [first_end, first_end], y = [0, 0.18], mode = "lines", name = "+Deviate"))

    fig.add_trace(go.Scatter(x = [sec_start, sec_start], y = [0, 0.18], mode = "lines", name = "-2Deviate"))

    fig.add_trace(go.Scatter(x = [sec_end, sec_end], y = [0, 0.18], mode = "lines", name = "+2Deviate"))

    fig.add_trace(go.Scatter(x = [three_start, three_start], y = [0, 0.18], mode = "lines", name = "-3Deviate"))

    fig.add_trace(go.Scatter(x = [three_end, three_end], y = [0, 0.18], mode = "lines", name = "+3Deviate"))

    fig.show()


if(score == "math score"):

    df = pd.read_csv("performance.csv")
    data = df["math score"].tolist()



    mean = sum(data)/len(data)
    stdev = statistics.stdev(data)
    median = statistics.stdev(data)
    mode = statistics.stdev(data)



    first_start, first_end = mean - stdev, mean + stdev
    sec_start, sec_end = mean - 2*stdev, mean + 2*stdev
    three_start, three_end = mean - 3*stdev, mean + 3*stdev

    listOfFirst = [result for result in data if result>first_start and result<first_end]

    listOf2 = [result for result in data if result>sec_start and result<sec_end]

    listOf3 = [result for result in data if result>three_start and result<three_end]

    print("{} % of data lies between 1 standard deviation and the mean ".format( len(listOfFirst) * 100.0/ len(data) ) )

    print("{} % of data lies between 2 standard deviation and the mean ".format( len(listOf2) * 100.0/ len(data) ) )

    print("{} % of data lies between 3 standard deviation and the mean ".format( len(listOf3) * 100.0/ len(data) ) )


    fig = ff.create_distplot([data], ["math scores"], show_hist = False)

    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.18], mode = "lines", name = "Mean"))

    fig.add_trace(go.Scatter(x = [first_start, first_start], y = [0, 0.18], mode = "lines", name = "-Deviate"))

    fig.add_trace(go.Scatter(x = [first_end, first_end], y = [0, 0.18], mode = "lines", name = "+Deviate"))

    fig.add_trace(go.Scatter(x = [sec_start, sec_start], y = [0, 0.18], mode = "lines", name = "-2Deviate"))

    fig.add_trace(go.Scatter(x = [sec_end, sec_end], y = [0, 0.18], mode = "lines", name = "+2Deviate"))

    fig.add_trace(go.Scatter(x = [three_start, three_start], y = [0, 0.18], mode = "lines", name = "-3Deviate"))

    fig.add_trace(go.Scatter(x = [three_end, three_end], y = [0, 0.18], mode = "lines", name = "+3Deviate"))

    fig.show()


if(score == "writing score"):

    df = pd.read_csv("performance.csv")
    data = df["writing score"].tolist()



    mean = sum(data)/len(data)
    stdev = statistics.stdev(data)
    median = statistics.stdev(data)
    mode = statistics.stdev(data)



    first_start, first_end = mean - stdev, mean + stdev
    sec_start, sec_end = mean - 2*stdev, mean + 2*stdev
    three_start, three_end = mean - 3*stdev, mean + 3*stdev

    listOfFirst = [result for result in data if result>first_start and result<first_end]

    listOf2 = [result for result in data if result>sec_start and result<sec_end]

    listOf3 = [result for result in data if result>three_start and result<three_end]

    print("{} % of data lies between 1 standard deviation and the mean ".format( len(listOfFirst) * 100.0/ len(data) ) )

    print("{} % of data lies between 2 standard deviation and the mean ".format( len(listOf2) * 100.0/ len(data) ) )

    print("{} % of data lies between 3 standard deviation and the mean ".format( len(listOf3) * 100.0/ len(data) ) )


    fig = ff.create_distplot([data], ["writing scores"], show_hist = False)

    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.18], mode = "lines", name = "Mean"))

    fig.add_trace(go.Scatter(x = [first_start, first_start], y = [0, 0.18], mode = "lines", name = "-Deviate"))

    fig.add_trace(go.Scatter(x = [first_end, first_end], y = [0, 0.18], mode = "lines", name = "+Deviate"))

    fig.add_trace(go.Scatter(x = [sec_start, sec_start], y = [0, 0.18], mode = "lines", name = "-2Deviate"))

    fig.add_trace(go.Scatter(x = [sec_end, sec_end], y = [0, 0.18], mode = "lines", name = "+2Deviate"))

    fig.add_trace(go.Scatter(x = [three_start, three_start], y = [0, 0.18], mode = "lines", name = "-3Deviate"))

    fig.add_trace(go.Scatter(x = [three_end, three_end], y = [0, 0.18], mode = "lines", name = "+3Deviate"))

    fig.show()