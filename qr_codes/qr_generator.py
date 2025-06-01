'''
This function takes two arguments to be passed:
url - which will be the page of the website
color which will be a choice a choice of red, blue, green, black
'''
import qrcode
# import click
import sys

#@click.command()
#@click.argument('url')


def print_help():
    """Print the module's docstring which contains usage instructions."""
    print(__doc__)

def generate_qr(url):
    if '//' in url:
        img_name = url.split(r'//',1)[1]
    else:
        img_name = url

    clean_img = img_name.replace('/','_')
    print(f'QR code will be saves as img_{clean_img}.png')
    
    img = qrcode.make(url)
    img.save(f'qr_code_{clean_img}.png')



def main():
    generate_qr(url)

if __name__ == '__main__':
    # Check if the user is asking for help
    if len(sys.argv) == 1 or '--help' in sys.argv or '-h' in sys.argv:
        print_help()
        sys.exit(0)
    else:
        url = sys.argv[1]        
    try:
        main()  # This will handle the CLI arguments
    except click.exceptions.UsageError:
        print_help()
        sys.exit(1)