import os, sys, random, time, subprocess

def generate_points(path, num, bbox):
    # bbox: minx, miny, maxx, maxy

    pts = [ (random.uniform(bbox[0], bbox[2]), random.uniform(bbox[1], bbox[3])) for _ in xrange(num) ]

    with open(path, 'wb') as f:
        for pt in pts:
            f.write("%f, %f\n" % (pt[0], pt[1]))
        #f.write("\n")

    print "Randomized %d points" % num

def generate(path, bbox):
    cmd = './build/main -i %s -w %d -h %d --nowrite' % (path, bbox[2] - bbox[0], bbox[3] - bbox[1])
    print cmd
    p = subprocess.Popen(cmd, cwd='.', shell=True)
    p.wait()
    if p.returncode != 0:
        print "Process failed!"
        sys.exit(1)


if __name__ == '__main__':

    maxcount = 0xffffffff
    if len(sys.argv) > 1:
        maxcount = int(sys.argv[1])

    initialseed = None
    if len(sys.argv) > 2:
        initialseed = int(sys.argv[2])

    path = "test.csv"
    bbox = (0, 0, 2048, 2048)
    count = 0
    while count < maxcount:
        print "Iteration", count
        count += 1

        seed = hash(time.time())
        if initialseed is not None:
            seed = initialseed
            initialseed = None
        random.seed(seed)
        print "Seed", seed

        generate_points(path, int(random.uniform(20000 + count * 2, 25000 + count * 4)), bbox)
        generate(path, bbox)

