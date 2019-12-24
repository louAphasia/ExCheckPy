from mrjob.job import MRJob

class RaitingCount(MRJob):
    def mapper(self, _, line):
        userId, movieId, rating, timestamp = line.split(",")
        if rating == "rating":
            yield
        result = [rating, 1]
        yield result;

    def reducer(self, key, value):
        result = [key,float(key) * sum(float*value)/ sum(value)]
        yield result

if __name__ == '__main__':
    RaitingCount.run()