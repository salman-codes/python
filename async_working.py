import asyncio
async def f1(r, d):
    print("Finding, within the range %s divisible by %s" % (r, d))
    l = []
    for i in range(r):
        if i % d == 0:
            l.append(i)

        if i % 100000 == 0:
            await asyncio.sleep(0.001)

    print("Done, %s is divisible by %s" % (r, d))
    return l


async def main():
    d1 = lp.create_task(f1(123312, 22145))
    d2 = lp.create_task(f1(309183, 4320))
    d3 = lp.create_task(f1(2200, 6))
    await asyncio.wait([d1, d2, d3])


if __name__ == '__main__':
    lp = asyncio.get_event_loop()
    lp.run_until_complete(main())
    lp.close()