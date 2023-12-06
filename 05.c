#include <stdio.h>
#include <inttypes.h>
#include <string.h>
#include <stdlib.h>

#define min(a, b) ((a) < (b) ? (a) : (b))

struct Range {
    uint64_t dst;
    uint64_t src;
    int dist;
};

struct Maps {
    struct Range blocks[100][100];
    int block_idx;
};

static uint64_t map_seed(struct Maps *data, uint64_t *seed, uint64_t *jump) {
    uint64_t end = UINT64_MAX;
    for (int i = 0; i < data->block_idx; i++) {
        for (int mapper_no = 0;; mapper_no++) {
            struct Range *range = &data->blocks[i][mapper_no];
            if (range->dist == 0)
                break;
            if (range->src <= *seed && *seed < range->src + range->dist) {
                end = min(range->dist - (*seed - range->src), end);
                *seed -= range->src;
                *seed += range->dst;
                break;
            }
        }
    }
    if (jump)
        *jump = end;
    return *seed;
}

static void parse_seeds(char *content, uint64_t *seeds, int *seed_idx) {
    char *cur;
    char *last = &content[7];
    do {
        cur = last;
        seeds[++(*seed_idx)] = strtoull(cur, &last, 10);
    } while (last != cur);
}

static inline void parse_ranges(char *content, struct Maps *data) {
    int ranges_idx = 0;
    char *line = strtok(content, "\n");
    while (line != NULL) {
        if (strchr(line, ':')) {
            ranges_idx = 0;
            data->block_idx++;
        } else if (strlen(line) > 1) {
            uint64_t src, dst, dist;
            sscanf(line, "%" SCNu64 " %" SCNu64 " %" SCNu64, &src, &dst, &dist);
            struct Range range = {src, dst, dist};
            data->blocks[data->block_idx - 1][(ranges_idx)++] = range;
        }
        line = strtok(NULL, "\n");
    }
}

int main() {
    FILE *fp = fopen("05.txt", "r");

    fseek(fp, 0, SEEK_END);
    long fp_size = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    char *contents = malloc(fp_size + 1);
    size_t bytes = fread(contents, 1, fp_size, fp);
    contents[fp_size] = '\0';

    struct Maps data;
    data.block_idx = 0;

    int seed_idx = -1;
    uint64_t seeds[100] = {};
    parse_seeds(contents, seeds, &seed_idx);

    parse_ranges(contents, &data);

    uint64_t ans = UINT64_MAX;
    for (int i = 0; i < seed_idx; i++) {
        uint64_t seed = seeds[i];
        uint64_t jump;
        uint64_t result = map_seed(&data, &seed, &jump);
        ans = min(result, ans);
    }
    printf("Part 1: %" PRIu64 "\n", ans);

    ans = UINT64_MAX;
    for (int i = 0; i < seed_idx; i += 2) {
        uint64_t pos = seeds[i];
        uint64_t end = pos + seeds[i + 1];
        while (pos < end) {
            uint64_t jump;
            uint64_t seed = pos;
            uint64_t result = map_seed(&data, &seed, &jump);
            ans = min(result, ans);
            pos += jump;
        }
    }
    printf("Part 2: %" PRIu64 "\n", ans);

    free(contents);
    fclose(fp);
    return 0;
}
