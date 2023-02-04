# TS2 Operator Analysis December 1, 2022 - Feburary 2, 2023

---

![WebLogo.png](https://github.com/zeekwired/Tristate/blob/3afaf79e6201849bc0266f78b1edf21112887f5c/WebLogo.png)

by Zach Dawson (TS2)

This is an analysis of each department and there performances throughout the months of Nov 2022-Feb 2023. This analysis will help gain insight of our departments progression and what problems need to be address in the future. This is a difficult task for a business to do without the proper tools to create visuals to better understand there trends and rankings within a company. 

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


![Operations by Department.png](https://github.com/zeekwired/Tristate/blob/d69b69dc7c515b9f386cf689c4ec7f2b99bec569/Operations%20by%20Department.png)

This visualization shows `Warehouse Pickers`, `Routes/Hotshot Pickers`, and `Outside Help (Shipping Department Employee's, Managers, etc)` compared against eachother, by Documents pulled, Lines Completed, and Units pulled each document. I will break each set of graphs by deparment to make this easier to process:

**Warehouse Pickers**:

**Docs**:

In the first bar plot, It is clear to see that `TBD` is dominating with the most documents pulled, at `4,538` picknotes. Following second to `TBD`, is `RLL` with `3,207` picknotes pulled. Others, in this graph that are full time pullers tend to average between `2,666` and `2,000` documents completed.

**Lines**:

Again, it would seem that `TBD` and `RLL` are leading the results of this graph. Note, the average line completed for other pullers seems to raise to `4,191` and `3,205`. Of course, lines on a picknote can vary depending on the weborder placed. However, if someone is experience lower average lines on an order could be represented by how many documents pulled by the operator.

**Units**:

It would appear that `TBD` and `RLL` are still the highest results. However, in this graph you can picture the amount of units from total documents completed. `ALT` for instance has lower documents and lines completed, but has the third highest units pulled. Even `NLS` with the lowest totals still manage to pull `6,183` units.

**Routes/Hotshot Pickers**:

**Docs**:

For this graph, it would appear that `JEH` and `MAT` are high ranking operators in this visualization. Note, that `JEH` and `MAT` are very similar in picknote completion.

**Lines**:

`JDH` in this visualization has a total line complete count of `2240`. This is the highest completion of lines in this category. 

**Units**:

Now for this graph you can tell there is a huge different in units being pulled by lines and documents. `HRB` pulled `11,195` units compared to pulling `720` picknotes and that accumulated `1,344` completed lines.

**Outside Help**:

For this section of graph it is everyone outside the Warehouse and Routes/Hotshot departments. 
![Warehouse Pullers VS Routes and HotShot.png](https://github.com/zeekwired/Tristate/blob/d69b69dc7c515b9f386cf689c4ec7f2b99bec569/Warehouse%20Pullers%20VS%20Routes%20and%20Hotshot.png)
![Operators by Units Received in Goods-In.png](https://github.com/zeekwired/Tristate/blob/d69b69dc7c515b9f386cf689c4ec7f2b99bec569/Operators%20by%20Units%20Received%20in%20Goods-In.png)
![Operators by lines per hour.png](https://github.com/zeekwired/Tristate/blob/d69b69dc7c515b9f386cf689c4ec7f2b99bec569/Operators%20by%20lines%20per%20hour.png)
