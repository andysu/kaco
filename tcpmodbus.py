from pyModbusTCP.client import ModbusClient
c = ModbusClient(host="91.222.19.222", port=402, auto_open=True)
regs = c.read_holding_registers(40001,8)
print(c.read_holding_registers(40094,2)[0]*65536+c.read_holding_registers(40094,2)[1])
