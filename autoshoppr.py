from lib import utils

a = utils.AmazonShoppr()

try:
    a.login()
    a.add_by_url('https://www.amazon.com/Chuck-Roast-Boneless-Pasture-Raised/dp/B07815GM3N/ref=sr_1_3', qty=3)
    a.add_by_url('https://www.amazon.com/365-Everyday-Value-Organic-Mediterranean/dp/B074H6YNLJ/ref=sr_1_3')
    a.add_by_url('https://www.amazon.com/Onion-Yellow-Organic-1-Each/dp/B07QV6B5WV/ref=sr_1_10', qty=2)
    a.add_by_url('https://www.amazon.com/365-Everyday-Value-Organic-Rainbow/dp/B07D6TD4VC/ref=sr_1_2')
    a.add_by_url('https://www.amazon.com/365-Everyday-Value-Organic-Broth/dp/B074H6QYL7/ref=sr_1_2')
    a.add_by_url('https://www.amazon.com/365-Everyday-Value-Organic-Thyme/dp/B074HBKSCL/ref=sr_1_2')
    a.add_by_url('https://www.amazon.com/365-Everyday-Value-Organic-Rosemary/dp/B074H6M37H/ref=sr_1_3')
    a.clean_exit()
except Exception:
    raise