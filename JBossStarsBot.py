from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import os

def start(bot, update):
    update.message.reply_text('Ahoy {}! Welcome to JBossStarsBot. \n\nTo get started, use the /stars command to fetch the stars from the GitHub repos of JBoss'.format(update.message.from_user.first_name))


def stars(bot, update):
    api = requests.get('https://api.github.com/orgs/JBossOutreach/repos')
    json = api.json()
    stars = ''
    for i in range(len(json)):
        stars = stars + '\n' + res[i]['name'] + ' : ' + str(res[i]['stargazers_count'])

    update.message.reply_text('Here\'s the list of all the JBoss repositories on GitHub along with their respective star count. \n\n' + stars + '\n\nTo get the stars of a specific repository, enter the name of the repository.')


def repo_stars(bot, update):
    api = requests.get('https://api.github.com/orgs/JBossOutreach')
    json = api.json()
    star = ''
    for i in range(len(json)):
        cur = res[i]['name']
        if cur == update.message.text:
            star = star + cur + ' : ' + str(res[i]['stargazers_count'])
        if cur == '':
            star = 'No such repository found.'

    bot.send_message(update.message.chat_id, star)

def main():
    TOKEN = '756573527:AAFr2VIuvp19xXgvHdt8w13qUP9DX4ESR9E'
    updater = Updater(TOKEN)
    PORT = int(os.environ.get('PORT', '8443')) 
    
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('stars', stars))
    dp.add_handler(MessageHandler(Filters.text, repo_stars))
    
    updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
    updater.bot.set_webhook("https://gcijbossbot.herokuapp.com/" + TOKEN)
    updater.idle()


  
if __name__ == '__main__':
    main()
