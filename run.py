from board import Board

def run_game():
    play_again=True
    while play_again:
        data=[['.' for i in range(7)] for j in range(6)]
        board=Board(data)
        board.display()
        color='red'
        color_map={'red':'blue','blue':'red'}
        count=0
        while board.running and count < 42:
            color=color_map[color]
            column=board.update_data(color)
            board.display()
            game_running=board.check_winner(column,color)
            count += 1
        print(f"Well Done {color}, you won!" )   
        play_again=input('Would you like to play again? (y/n) ')=='y'
    
run_game()

