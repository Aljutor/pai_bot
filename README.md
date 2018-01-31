# pai_bot
Telegram bot for first task during PAI course

Select bot mode by using one of cmd:
```
/start   - return to start menu
/talk    - talk mode (can solve simple math) 
/matches - 21 matches game
/xo3     - classic 3x3 TicTacToe game
/xo5     - TicTacToe on 10x10 filed, 5 in row
```

Game state saved (until bot restart).  
After game over use command again to start new game.  
You can switch between modes on the fly   
Use /start to return in menu.  


To start bot:
```
docker build -t bot-pai .

docker run \
--env WA_TOKEN=<wolfram_alpha_token> \ 
--env BOT_TOKEN=<telegram_token> \
--name bot-pai --rm bot-pai
```
