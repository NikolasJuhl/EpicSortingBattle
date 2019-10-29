import time, json, sys, sorteringsAlgoritmer as algo

def importFile(filename):
    outList = []
    fil = open(filename)
    for line in fil:
        outList.append(line.strip())
    return outList

def runTestCase(filename):
    caseResults = {}
    print('\nImporterer', filename)
    case = importFile('./testfiles/' + filename)

    print('Starter Select Sort')
    tStart = time.time()
    algo.selectionSort(case)
    tSlut = time.time()
    caseResults['Select Sort'] = tSlut - tStart
    print('Select Sort:', tSlut - tStart, 'sekunder')

    print('Starter Insert Sort')
    tStart = time.time()
    algo.insertionSort(case)
    tSlut = time.time()
    caseResults['Insert Sort'] = tSlut - tStart
    print('Insert Sort:', tSlut - tStart, 'sekunder')

    print('Starter Bubble Sort')
    tStart = time.time()
    algo.bubbleSort(case)
    tSlut = time.time()
    caseResults['Bubble Sort'] = tSlut - tStart
    print('Bubble Sort:', tSlut - tStart, 'sekunder')

    print('Starter MergeSort')
    tStart = time.time()
    algo.mergeSort(case)
    tSlut = time.time()
    caseResults['MergeSort'] = tSlut - tStart
    print('MergeSort:', tSlut - tStart, 'sekunder')

    print('Starter Timsort')
    tStart = time.time()
    case.sort()
    tSlut = time.time()
    caseResults['Timsort'] = tSlut - tStart
    print('Timsort:', tSlut - tStart, 'sekunder')

    return caseResults

testResults = {}
totalTimeStart = time.time()
for run in range(10):
    runResults = {}
    runResults['Testcase 0'] = runTestCase('testcase0.txt')
    runResults['Testcase 1'] = runTestCase('testcase1.txt')
    runResults['Testcase 2'] = runTestCase('testcase2.txt')
    runResults['Testcase 3'] = runTestCase('testcase3.txt')
    runResults['Testcase 4'] = runTestCase('testcase4.txt')
    testResults[run] = runResults
totalTimeSlut = time.time()
print('\n\nTotal tid: ', totalTimeSlut - totalTimeStart, 'sekunder')

fil = open('testresults.txt', 'w')
fil.write(json.dumps(testResults))
fil.close()
