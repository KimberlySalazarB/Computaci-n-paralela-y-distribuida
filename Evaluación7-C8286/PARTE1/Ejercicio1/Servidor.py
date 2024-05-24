# Servidor

import asyncio
import pickle
import nest_asyncio
nest_asyncio.apply()


results = {}

async def submit_job(reader, writer):
    job_id = max(list(results.keys()) + [0]) + 1
    writer.write(job_id.to_bytes(4, 'little'))
    await writer.drain()
    data_length = int.from_bytes(await reader.read(4), 'little')
    data = pickle.loads(await reader.read(data_length))
    results[job_id] = sum(data)

async def get_results(reader, writer):
    job_id = int.from_bytes(await reader.read(4), 'little')
    result = results.get(job_id)
    if result is not None:
        result_data = pickle.dumps(result)
        writer.write(len(result_data).to_bytes(4, 'little'))
        writer.write(result_data)
    else:
        writer.write((0).to_bytes(4, 'little'))
    await writer.drain()

async def accept_requests(reader, writer):
    op = await reader.read(1)
    if op[0] == 0:  # Recibir lista de números y calcular suma
        await submit_job(reader, writer)
    elif op[0] == 1:  # Recibir resultado
        await get_results(reader, writer)

async def main():
    server = await asyncio.start_server(accept_requests, '127.0.0.1', 1936)
    async with server:
        await server.serve_forever()

asyncio.run(main())