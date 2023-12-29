class LossyCount:
    def __init__(self, frequency_treshold, error):
        self.__frequency_treshold = frequency_treshold
        self.__error = error
        self.__indivual_frequencies = {}
        self.__individual_maximumError = {} 
        self.__currentBucket = [] 
        self.__idCurrentBucket = 1
        self.__processedDataCounter = 0

    # starting point of the pipeline
    # receive the data to be processed and create the buckets
    # the datastream is a single string
    def processDatastream(self, datastream):
        for data in datastream:
            self.__currentBucket.append(data)

            if len(self.__currentBucket) >= (1 / self.__error):
                self.__processBucket()
                self.__currentBucket = []
                self.__idCurrentBucket += 1

    # process data in current bucket
    # after finishing, decreases the counters and 
    # removes those that meet the requirements 
    def __processBucket(self):
        for data in self.__currentBucket:
            self.__processedDataCounter += 1
            self.__processIndividualData(data)

        self.__decrementCounters()
        self.__pruneFrequencies()

    # process individual pieces of the datastream
    # checks if it is already in the frequencies dict
    # if it is, it increments its counter
    # if not, it creates a new entry in the frequencies dict and the max error dict 
    def __processIndividualData(self, data):
        if data in self.__indivual_frequencies:
            self.__indivual_frequencies[data] += 1
        else:
            self.__indivual_frequencies[data] = 1
            self.__individual_maximumError[data] = self.__idCurrentBucket - 1

    # decrements the counters of every entry in the frequencies dict
    def __decrementCounters(self):
        for data in self.__indivual_frequencies.keys():
            self.__indivual_frequencies[data] -= 1

    # for every entry in the frequencies dict, 
    # checks if the condition for deletion is met,
    # deleting those that are ready to delete
    def __pruneFrequencies(self):
        to_remove = []

        for key, value in self.__indivual_frequencies.items():
            if value + self.__individual_maximumError[key] <= self.__idCurrentBucket:
                to_remove.append(key)

        for key in to_remove:
            del self.__indivual_frequencies[key]
            del self.__individual_maximumError[key]

    # get the results of the counter
    # can get the whatever top counters
    def getResults(self, top=5):
        to_return = {k:v for k, v in self.__indivual_frequencies.items()\
                if v >= (self.__frequency_treshold - self.__error) * self.__processedDataCounter}
        
        sorted_count = dict(sorted(to_return.items(), key=lambda item: item[1], reverse=True))
        return dict(list(sorted_count.items())[:top])

