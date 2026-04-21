:- dynamic disease/1.
symptom_present(fever).
symptom_present(cough).
rule(flu) :-
symptom_present(fever),
symptom_present(cough).
rule(common_cold) :-
symptom_present(sneezing),
symptom_present(runny_nose).
rule(covid_19) :-
symptom_present(fever),
symptom_present(cough),
symptom_present(loss_of_taste).
diagnose :-
rule(Disease),
\+ disease(Disease),
assert(disease(Disease)),
write('The patient may have '),
write(Disease), write('.'), nl,
!.
diagnose :-
write('No matching disease found.'), nl.

Op
?- diagnose
?- symptom_present(fever)
?- symptom_present(cough)
?- symptom_present(sneezing)