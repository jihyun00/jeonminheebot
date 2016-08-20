from plan import Plan


cron = Plan()

cron.command('date', every='weekend')
cron.command('', every='')

if __name__ == '__main__':
    cron.run()
