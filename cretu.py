import base64
import random
from seleniumbase import SB

# Decode channel name
name = "YnJ1dGFsbGVz"
fulln = base64.b64decode(name).decode("utf-8")

urlt = f"https://www.twitch.tv/{fulln}"

while True:
    with SB(uc=True, locale="en", ad_block=True, chromium_arg='--disable-webgl') as bot:

        wait_time = random.randint(450, 800)

        bot.activate_cdp_mode(urlt)
        bot.sleep(2)

        # Accept cookies
        if bot.is_element_present('button:contains("Accept")'):
            bot.cdp.click('button:contains("Accept")', timeout=4)

        bot.sleep(12)

        # Start watching if needed
        if bot.is_element_present('button:contains("Start Watching")'):
            bot.cdp.click('button:contains("Start Watching")', timeout=4)
            bot.sleep(10)

        # Accept again if Twitch shows another popup
        if bot.is_element_present('button:contains("Accept")'):
            bot.cdp.click('button:contains("Accept")', timeout=4)

        # Check if stream is live
        if bot.is_element_present("#live-channel-stream-information"):

            # Open a second driver
            bot2 = bot.get_new_driver(undetectable=True)
            bot2.activate_cdp_mode(urlt)
            bot2.sleep(10)

            if bot2.is_element_present('button:contains("Start Watching")'):
                bot2.cdp.click('button:contains("Start Watching")', timeout=4)
                bot2.sleep(10)

            if bot2.is_element_present('button:contains("Accept")'):
                bot2.cdp.click('button:contains("Accept")', timeout=4)

            bot.sleep(wait_time)

        else:
            break
