#Exam Questions <img src="../../Resources/exam.png" width=50px alt="Tick Sheet">

##Instructions
Edit this document and answer the questions in the sections surrounded by ```.

There are 30 marks available and are awarded grades as follows:

|Score|Grade|
|-----|-----|
|<6|U|
|6+|G|
|9+|F|
|12+|E|
|15+|D|
|18+|C|
|21+|B|
|24+|A|
|27+|A*|


##Data Representation

###1 - Why do we represent data using binary when using computers *(1 mark)*

```
We use binary because it takes up less space than denary and can only have 2 values
```
###2 - How would we represent the number 147 in binary? *(1 mark)*
```
10010011
```
###3 - Can you convert the hexadecimal number **b5** to denary, there is a mark for you working. *(2 marks)*
```
B = 11, 5 = 5
11 = 1011
5 = 0101
B5 = 10110101
```
###4 - Here is a function written is **pseudocode**.
```
FUNCTION validUser (users , user)
    FOR x <-1 to LEN(users)
        IF users[x] = user
			RETURN True
		ENDIF
	ENDFOR
	RETURN False
ENDFUNCTION
```

(a) What type of data is **users**? **(1 mark)**
```
A list or tuple
```

(b) What type of data is returned by this function? **(1 mark)**
```
A string
```

##Errors
###6 - This program is supposed to find the mean of a list of numbers and print it out for the user:
```
line1:		tot <- 0
line2:		nums <- [1,6,4,2,5,3]
line3:		FOR x <- to LEN(nums)
line4:			tot <- nums[x]
line5:		ENDFOR
line6:		mean <- tot
line7:		OUTPT mean
```

(a) On which line is there a **syntax** error? **(1 mark)**
```
line 7
```

(b) What is meant by a **syntax** error? **(1 mark)**
```
An error caused by an incorrectly spelt function or keyword.
```

(c) Identify a logical error in the program and suggest how this might be fixed. **(2 marks)**
```
On line 6 mean becomes tot, this should be "mean <- tot/LEN(nums)"
```

(d) Describe and give an example of the 3rd kind of programming error. **(2 marks)**
```
A run time error is an error that occurs while the program is running.
```

##Algortithms
###7 - Write an **algorithm** that if given a list of numbers could find the largest. Try to use [pseudocode](http://filestore2.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF).
```

    nums = list(numbers)
    FOR x TO range(LEN(nums)):
        for y in range(i+1, LEN(nums)):
            IF numbers[y] < numbers[x]:
                numbers[y], numbers[x] <- numbers[x], numbers[y]
    	    ENDIF
    	ENDFOR
    ENDFOR
    	
    print numbers
```

##Networking
###8 - Research the following methods (*topologies*) for connecting devices to a network. In each case give a description and at least 1 advantage and 1 disadvantage.

**Bus Topology (6 marks)**
```
Describe: A bus network where nodes are connected in a daisy chain by a linear sequence of buses

Advantages: 
	Easy to connect a computer to a linear bus
	requires less cable length than a star topology
	Works well for smaller networks

Disadvantages:
	Entire network shuts down if theres a break in the cable
	Terminators are needed at both ends of the backbone cable
	Difficult to identify the problem if the entire network shutsdown
	Not ment to be used as a stand alon solution in a large building
	Slower as more devices are added
```

**Ring Topology (6 marks)**
```
Describe: Each node attatches itself to two other nodes to form a ring

Advantages: 
	Orderly, every device has acess to the token
	Performs better than a bus topology under heavy load
	Does not require a central node
	Easy to identify faults
	quite easy to install and configure
	

Disadvantages:
	One malfunctioning workstation can create probelsm for the entire network
	Moving, adding and changing devices can affect the network
	Communication delay is linked to the number of nodes on the network
	Bandwith is shared
	More difficult to configure
```

**Star Topology (6 marks)**
```
Describe: One central hub links to each of the other nodes

Advantages:
	Better performace
	Isolation of devices
	Benefits from centralization
	Easy to detect faults
	No distruptions to the network when adding or removing devices
	Installation is easy as each device only needs a link and one input/output port

Disadvantages:
	Whole network depends on one hub
	Communication must pass through central hub, meaning that if the hub is compromised then so is all communication
```
