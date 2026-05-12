import sys, os, struct

txt, limit, outdir, name = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
written = skipped = 0

os.makedirs(outdir, exist_ok=True)

with open(txt, encoding='utf-8') as words:
    with open(os.path.join(outdir, f'{name}.bytes'), 'wb') as tensors:
        with open(os.path.join(outdir, f'{name}.tsv'), 'w', encoding='utf-8', newline='\n') as metadata:
            dim = int(words.readline().split()[1])
            metadata.write('word\trank\n')
            for line in words:
                if written >= limit:
                    break
                parts = line.rstrip().rsplit(' ', dim)
                if len(parts) != dim + 1:
                    skipped += 1
                    continue
                tensors.write(struct.pack(f'<{dim}f', *map(float, parts[1:])))
                metadata.write(f'{parts[0]}\t{written}\n')
                written += 1

print(f'{name}: {written} words, {skipped} skipped, tensor_shape: [{written}, {dim}]')
