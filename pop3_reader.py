import poplib

import click
import tqdm

FROM = "pop3_reader"


@click.command()
@click.option('--pop3_host', default='pop.gmail.com', required=True, type=str)
@click.option('--username', required=True, type=str)
@click.option('--password', prompt=True, required=True, type=str)
@click.option(
    '--mbox-file',
    default='inbox.mbox',
    required=True,
    type=str,
    help='Output file for Mbox (default is inbox.mbox)',
)
@click.option(
    '--commit',
    default=False,
    is_flag=True,
    type=bool,
    help='Skip performing QUIT command to keep messages "touched"',
)
@click.option(
    '--dry-run',
    default=False,
    is_flag=True,
    type=bool,
    help='Do not actually download messages',
)
def pop3(pop3_host, username, password, mbox_file, commit, dry_run):
    print(f"- connecting to {pop3_host} as {username}")
    server = poplib.POP3_SSL(pop3_host)
    server.user(username)
    server.pass_(password)
    pop3info = server.stat()

    mail_count = pop3info[0]
    print(f"- downloading {mail_count} message(s)")

    with open(mbox_file, 'w') as mbox_file:
        indexes = list(reversed(range(mail_count)))
        with tqdm.tqdm(
            total=len(indexes),
            desc="- downloading",
            bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}]',
        ) as pbar:
            for i in indexes:
                if not dry_run:
                    print(f"From {FROM}", file=mbox_file)
                    for message in server.retr(i + 1)[1]:
                        print(message.decode(), file=mbox_file)
                    print(file=mbox_file)
                pbar.update(1)
            if commit:
                print("- marking messages as read")
                server.quit()  # prevent marking messages as read
    print("- done")


if __name__ == "__main__":
    pop3()
