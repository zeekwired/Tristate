# TS2 Operator Analysis December 1, 2022 - Feburary 2, 2023

---

![WebLogo.png](https://github.com/zeekwired/Tristate/blob/3afaf79e6201849bc0266f78b1edf21112887f5c/WebLogo.png)

by Zach Dawson (TS2)

This is an analysis of each department and their performances throughout the months of Nov 2022-Feb 2023. By analysing our departments' progress, we can gain insight into future problems. Creating visuals to understand trends and rankings within a company is difficult for a business without the proper tools.

Data Source:

This data source was collected from Autopart's WMS Operator Analysis (Native WMS System Tri-State Enterprises, Inc operates on).

Data Dictionary:


|     Features          |     Description                                                                                        |
|-----------------------|--------------------------------------------------------------------------------------------------------|
|     Oper              |     This column represents the operator code assigned to employee when on boarding.                    |   
|     Name              |     Name of employee's.                                                                                | 
|     Lines             |     How many lines are completed from documents/PO orders from operator.                               |   
|     Lines %           |     This is the total percentage of lines completed by operator.                                       |   
|     Units             |     How many units from documents that operator pulled or stocked.                                     |   
|     Units %           |     Percentage of units an operator has pulled or stocked.                                             |  
|     Avg. Unit Time    |     Average time a unit is pulled or stocked from an operator.                                         |   
|     Docs              |     This represents how many documents the operator has completed (Picknotes/PO Orders).               |   
|     Total Time        |     This column is the total amount of time that the operator used Picking adhoc, Goods-In, or Putaway.| 
|     Lines/Hr          |     This calculates the average lines per hour an operator has completed.                              |   
|     Avg Lines         |     Average amount of lines completed by operator.                                                     |

# Pickers

---

# Picking Operations by Department
![Operations by Department.png](https://github.com/zeekwired/Tristate/blob/d69b69dc7c515b9f386cf689c4ec7f2b99bec569/Operations%20by%20Department.png)

This visualization shows `Warehouse Pickers`, `Routes/Hotshot Pickers`, and `Outside Help (Shipping Department Employee's, Managers, etc)` compared against eachother, by Documents pulled, Lines Completed, and Units pulled each document. I will break each set of graphs by deparment to make this easier to process:

# **Warehouse Pickers**:

## **Docs**:

In the first bar plot, It is clear to see that `TBD` is dominating with the most documents pulled, at `4,538` picknotes. Following second to `TBD`, is `RLL` with `3,207` picknotes pulled. Others, in this graph that are full time pullers tend to average between `2,666` and `2,000` documents completed.

## **Lines**:

Again, it would seem that `TBD` and `RLL` are leading the results of this graph. Note, the average line completed for other pullers seems to raise to `4,191` and `3,205`. Of course, lines on a picknote can vary depending on the weborder placed. However, if someone is experience lower average lines on an order could be represented by how many documents pulled by the operator.

## **Units**:

It would appear that `TBD` and `RLL` are still the highest results. However, in this graph you can picture the amount of units from total documents completed. `ALT` for instance has lower documents and lines completed, but has the third highest units pulled. Even `NLS` with the lowest totals still manage to pull `6,183` units.

# **Routes/Hotshot Pickers**:

## **Docs**:

For this graph, it would appear that `JEH` and `MAT` are high ranking operators in this visualization. Note, that `JEH` and `MAT` are very similar in picknote completion.

## **Lines**:

`JDH` in this visualization has a total line complete count of `2240`. This is the highest completion of lines in this category. 

## **Units**:

Now for this graph you can tell there is a huge different in units being pulled by lines and documents. `HRB` pulled `11,195` units compared to pulling `720` picknotes and that accumulated `1,344` completed lines.

# **Outside Help**:

For this section of graph it is everyone outside the Warehouse and Routes/Hotshot departments. 

---

# Warehouse Pullers VS. Routes/Hotshot 
![Warehouse Pullers VS Routes and HotShot.png](https://github.com/zeekwired/Tristate/blob/d69b69dc7c515b9f386cf689c4ec7f2b99bec569/Warehouse%20Pullers%20VS%20Routes%20and%20Hotshot.png)

# **WareHouse Pullers**:

## **Lines/Hr**:

It appears that unlike in the last visualiztion `TLZM`, `ALT`, and `AXA` are the highest ranking operators. `ALT` seems to be the fastest full-time puller averaging `60 lines/Hr`. Even though, `TBD` and `RLL` dominated the visualization scoring the highest rank. It would appear that speed and how many lines per hour an operator obtains.

# **Routes/Hotshot**:

## **Lines/Hr**:

For Routes/Hotshot, `JEH` has an average of `47` lines/Hr, while `MAT` has and average of `22` lines/Hr.

The other graphs give the same results as the ones above in `Operations by Department` in percentages.

# Units by Total Time by Operator
![Pulling Shift.png](https://github.com/zeekwired/Tristate/blob/2c3d66c3d6bd0139be86c950416234adbafbf4ff/Pulling%20shifts.png)

# Warehouse Pickers:
Looking at the amount of units being pulled by time. `TBD` has the second highest hours worked but also the highest units pulled. Note that `FLB` has the second highest hours worked, but has one of the lowest units pulled total.

# Routes/Hotshot:
In this graph it seems that `MAT` seems to have worked the most hours in picking adhoc. Dispite having these hours it seems like `HRB` tends to pull more units in a shorten time spent in picking adhoc.

# Outside Help:
This represents the amount of outside help from different departments within TS2.
---
# Stockers
---

# Operators by Units Received in Goods-in
![Operators by Units Received in Goods-In.png](https://github.com/zeekwired/Tristate/blob/d69b69dc7c515b9f386cf689c4ec7f2b99bec569/Operators%20by%20Units%20Received%20in%20Goods-In.png)
# Night Shift
Judging by the graph it seems that `JBC` and `TLH` are the top stockers on the night crew. Averaging between 7,000 and 8,000 units seems to be the range for stockers within this date range.

# Day Shift
Day crew `BSE` seems to lead the team in the number of units stocked. The amount of units being stocked by `BSE` can also be compared to the amount of units `RAH` is stocking on the night shift. In the event that BSE were to move to night shift, his performance could be compared with that of the third highest performing night shift stocker.

# Pullers
Out of the pullers `FLB` has the highest units stocked. Pickers are not subject to this analysis for stockers but this could help for future insight on decisions to reward operators at the end of the month.

# Others
This visual represents operators outside the scope of the other three graphs.
---

# Operators by Lines/Hr in Goods-In
![Operators by lines per hour.png](https://github.com/zeekwired/Tristate/blob/d69b69dc7c515b9f386cf689c4ec7f2b99bec569/Operators%20by%20lines%20per%20hour.png)
# Night Shift
`RAH` seems to be leading the stockers with 59 lines per hour. It seems the average of the lines per hour in the nights shift crew is between 24-29 lines. Understanding the averages of employee work speed can help determine what qouta can be acheived.
# Day Shift
This graph is interesting. Our top ranking stockers in day shift to have the most units stocked is `BSE` and `GDM`. However, in this visualization it seems that both operators have the lowest lines per hour.
# Pullers
This graph represents what the speed of the pullers stocking to see if they can compete with day and night shift.
# Others
This is a visualization that shows operators outside of department.
---
# Units by Total Time in Goods-In
![Stocking Shifts.png](https://github.com/zeekwired/Tristate/blob/30a0c3e0a1af2267b3bcaea5bc87b03f399af0c3/Stocking%20Shifts.png)
