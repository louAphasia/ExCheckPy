from mrjob.job import MRJob

class RaitingCount(MRJob):
    def mapper(self, _, line):
        userId, movieId, rating, timestamp = line.split(",")
        if movieId != "movieId":
            yield movieId, float(rating)

    def reducer(self, key, ratings):
        count = 0
        sum = 0
        for rating in ratings:
            sum += rating
            count += 1

        if count == 0:
            yield key,0
        else:
            yield [key, sum/count]

if __name__ == '__main__':
    RaitingCount.run()