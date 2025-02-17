from web3 import Web3
import requests
import json

# Подключаемся к публичному Ethereum-узлу (например, Infura)
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY"
w3 = Web3(Web3.HTTPProvider(infura_url))

# Проверяем подключение
if not w3.is_connected():
    print("Ошибка: не удалось подключиться к Ethereum")
    exit()

# Введи адрес NFT контракта и ID токена
nft_contract_address = "0x1234567890abcdef1234567890abcdef12345678"  # Заменить на реальный контракт
nft_token_id = 1  # ID NFT токена

# ABI для стандартных ERC-721 контрактов
erc721_abi = '[{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"tokenURI","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]'

# Подключаемся к NFT-контракту
nft_contract = w3.eth.contract(address=w3.to_checksum_address(nft_contract_address), abi=json.loads(erc721_abi))

# Получаем URI метаданных
try:
    token_uri = nft_contract.functions.tokenURI(nft_token_id).call()
    print(f"Metadata URI: {token_uri}")

    # Загружаем метаданные
    response = requests.get(token_uri)
    if response.status_code == 200:
        metadata = response.json()
        print("NFT Metadata:")
        print(json.dumps(metadata, indent=4))
    else:
        print("Ошибка при загрузке метаданных")
except Exception as e:
