<div align="center">

# 🐍 Python Security Tools

**Offensive & defensive helper tools written in pure Python**

</div>

---

## Tools

| Tool | Type | Description |
|------|------|-------------|
| `port_scanner.py` | Offensive | Multi-threaded TCP port scanner |
| `hash_identifier.py` | Offensive | Identify common hash types |
| `banner_grabber.py` | Offensive | Simple service banner grabber |
| `log_analyzer.py` | Defensive | Basic failed login / auth.log analyzer |

## Usage Examples

```bash
# Port scan
python port_scanner.py 192.168.1.10

# Identify hash
python hash_identifier.py 5f4dcc3b5aa765d61d8327deb882cf99

# Banner grab
python banner_grabber.py 192.168.1.10 22
```

## Disclaimer

These tools are intended for **authorized testing and educational purposes only**.  
Do not use them against systems you do not own or have explicit permission to test.

## License

MIT
