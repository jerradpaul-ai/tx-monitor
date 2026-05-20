import requests
from datetime import datetime

def get_tx_data():
    url = "https://api.coingecko.com/api/v3/coins/tx"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        price = data['market_data']['current_price']['usd']
        market_cap = data['market_data']['market_cap']['usd']
        volume_24h = data['market_data']['total_volume']['usd']
        change_24h = data['market_data']['price_change_percentage_24h']
        
        your_balance = 6900000
        your_value_usd = your_balance * price
        your_value_cad = your_value_usd * 1.38  # approx current CAD rate
        
        print(f"\n=== TX MONITOR - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
        print(f"Price: ${price:.5f} USD ({change_24h:+.2f}% 24h)")
        print(f"Market Cap: ${market_cap:,.0f}")
        print(f"24h Volume: ${volume_24h:,.0f}")
        print(f"\nYOUR 6.9M TX POSITION:")
        print(f"   USD: ${your_value_usd:,.0f}")
        print(f"   CAD: ${your_value_cad:,.0f} (approx)")
        print(f"\n💡 Tip: Check explorer.tx.org for latest blocks/transactions and staking.")
        print("   Watch PSE distribution for unlocks.")
        
        return data
    except Exception as e:
        print("Error fetching data:", e)
        return None

if __name__ == "__main__":
    get_tx_data()
