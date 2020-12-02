from thycotic.secrets.server import SecretServer

secret_server = SecretServer("https://secretserverurl/SecretServer","username", "password", "domain")

secret = secret_server.get_secret(1)

print(secret)