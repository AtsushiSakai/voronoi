#define JC_VORONOI_IMPLEMENTATION
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// If you wish to use doubles
#define JCV_REAL_TYPE double
#define JCV_FABS fabs
#define JCV_ATAN2 atan2

#include "jc_voronoi.h"
#include "invalid_data.h"

int main(int argc, const char** argv)
{
    int count = sizeof x / sizeof x[0];
    printf("count:%d", count);

    jcv_point* points = (jcv_point*)malloc( sizeof(jcv_point)*count );
    for( uint64_t i = 0; i < count; ++i ){
        points[i].x = x[i];
        points[i].y = y[i];
    }

    jcv_diagram diagram;
    memset(&diagram, 0, sizeof(jcv_diagram));
    // assersion error
    // Assertion failed: (internal->numsites == 1), function jcv_fillgaps, file src/jc_voronoi.h, line 1143.
    jcv_diagram_generate(count, points, 0, 0, &diagram );
    jcv_diagram_free( &diagram );

    return 0;
}

