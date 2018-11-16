from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

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
    updater = Updater('715343706:AAFKBe_vR3StWErxr-j1UlTZM6qUhwzlMHY')
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('stars', stars))
    dp.add_handler(MessageHandler(Filters.text, repo_stars))
    
    updater.start_polling()
    updater.idle()

  
if __name__ == '__main__':
    main()
