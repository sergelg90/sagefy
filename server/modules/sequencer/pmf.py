"""
PMF, or Probability Mass Function.
"""


class PMF(object):
    def __init__(self, hypotheses=None):
        """
        Create a new PMF, given a list of hypotheses.
        Internally, hypotheses is a dict of hypo: probability.
        """

        if isinstance(hypotheses, (tuple, list)):
            self.hypotheses = {hypothesis: 1 for hypothesis in hypotheses}
        elif isinstance(hypotheses, dict):
            self.hypotheses = hypotheses
        else:
            self.hypotheses = {}
        self.normalize()

    def update(self, data):
        """
        Main update function. Updates each hypothesis based on the
        data provided.
        """

        self.hypotheses = {hypothesis:
                           probability * self.likelihood(data, hypothesis)
                           for hypothesis, probability
                           in self.hypotheses.items()}
        self.normalize()
        return self

    def likelihood(self, data, hypothesis):
        """
        What is the likelihood of getting this data, given the
        particular hypothesis?
        **This is function should be overwritten.**
        """

        raise Exception("No method implemented.")

    def normalize(self):
        """
        Make sure that all hypotheses sum up to 1.
        """

        total = sum(probability
                    for hypothesis, probability
                    in self.hypotheses.items())
        self.hypotheses = {hypothesis:
                           probability / total
                           for hypothesis, probability
                           in self.hypotheses.items()}
        return self

    def get_value(self):
        """
        Turns the distribution into a single value.
        Tends to fall inbetween the mode and the mean,
        but fares better earlier on than either.
        """

        return sum(hypothesis * probability
                   for hypothesis, probability
                   in self.hypotheses.items())
