prior(sunny, 0.5).
prior(rainy, 0.3).
prior(cloudy, 0.2).
likelihood(cloudy, sunny, 0.2).
likelihood(cloudy, rainy, 0.7).
likelihood(cloudy, cloudy, 0.9).
likelihood(humidity, sunny, 0.3).
likelihood(humidity, rainy, 0.8).
likelihood(humidity, cloudy, 0.6).
evidence_prob(Evidence, Total) :-
findall(P,
(prior(W, Prior),
likelihood(Evidence, W, L),
P is Prior * L),
List),
sum_list(List, Total).
bayes(Weather, Evidence, Posterior) :-
prior(Weather, Prior),
likelihood(Evidence, Weather, Likelihood),
evidence_prob(Evidence, Total),
Posterior is (Prior * Likelihood) / Total.

Query
bayes(sunny, cloudy, P).