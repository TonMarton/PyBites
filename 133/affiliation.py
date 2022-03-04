def generate_affiliation_link(url: str):
    
    return f'http://www.amazon.com/dp/{url.split("/dp/")[1].split("/")[0]}/?tag=pyb0f-20'