import textwrap
import sys
import subprocess

def main():
    if len(sys.argv) != 3:
        print('Usage: python3 openssl-cert-formatter.py "fullstring" "cert.pem"')
        return

    long_string = sys.argv[1]
    output_filename = sys.argv[2]

    # Wrap the long string to 64 characters per line
    wrapped_key = textwrap.fill(long_string, width=64)

    # PEM header and footer
    header = "-----BEGIN CERTIFICATE-----"
    footer = "-----END CERTIFICATE-----"

    # Combine everything into the PEM format
    pem_key = f"{header}\n{wrapped_key}\n{footer}"

    # Write the formatted key to the specified filename
    with open(output_filename, 'w') as cert_file:
        cert_file.write(pem_key)

    print(f"Formatted key saved to {output_filename}")

    # Now compute the fingerprint of the saved certificate
    try:
        output = subprocess.check_output(['openssl', 'x509', '-noout', '-fingerprint', '-in', output_filename], stderr=subprocess.STDOUT, universal_newlines=True)
        print(output.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error running OpenSSL command: {e.output.strip()}")

if __name__ == '__main__':
    main()
