import logging
from src.core.config import Config
from src.core.device_manager import DeviceManager
from src.bypass.bypass_manager import BypassManager

logging.basicConfig(level=logging.DEBUG)

config = Config()

# Initialize device manager
print('Initializing device manager...')
dm = DeviceManager(config)
print('ADB path:', dm.adb_path)
print('Fastboot path:', dm.fastboot_path)

# Scan devices
print('Scanning devices...')
devices = dm.scan_devices()
print('Devices found:', len(devices))
if not devices:
    raise SystemExit('No devices found. Connect device and enable USB debugging.')

for d in devices:
    print('  serial', d.serial, 'type', d.connection_type, 'model', d.model, 'manu', d.manufacturer)

# Choose the first device
device = devices[0]

# Initialize bypass
print('Initializing bypass manager...')
manager = BypassManager(config, dm)
methods = manager.get_recommended_methods(device)
print('Recommended methods:', [m.name for m in methods[:5]])
if not methods:
    raise SystemExit('No bypass methods available for device.')

method = methods[0]
print('Executing method:', method.name)
manager.progress_callback = lambda msg, p: print(f'PROGRESS {p}%: {msg}')
result = manager.execute_method(method, device)
print('Bypass result:', result)

print('Verifying bypass state...')
verify = manager._verify_bypass_success(device)
print('Verification result:', verify)
