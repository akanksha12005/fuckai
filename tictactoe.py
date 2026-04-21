% Winning conditions
win(Player, Board) :-
Board = [Player, Player, Player, _, _, _, _, _, _];
Board = [_, _, _, Player, Player, Player, _, _, _];
Board = [_, _, _, _, _, _, Player, Player, Player];
Board = [Player, _, _, Player, _, _, Player, _, _];
Board = [_, Player, _, _, Player, _, _, Player, _];
Board = [_, _, Player, _, _, Player, _, _, Player];
Board = [Player, _, _, _, Player, _, _, _, Player];
Board = [_, _, Player, _, Player, _, Player, _, _].
% Check free position
free(Position, Board) :-
nth0(Position, Board, empty).
% Select best move (first free position)
best_move(Board, Move) :-
free(Move, Board), !.
Query
best_move([x,o,x,empty,o,empty,empty,empty,x], Move).
win(x, [x,x,x,empty,o,empty,o,empty,o]).
win(o, [x,o,x,empty,o,empty,empty,o,x]).