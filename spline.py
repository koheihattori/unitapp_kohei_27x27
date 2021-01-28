def __spline_smoothing_kernel(x, d: float):
    # piecewise function is not supported on CuPy
    # value = np.piecewise(x,
    #                      [
    #                          (- d * 1.5 < x) * (x < - d * 0.5),
    #                          (- d * 0.5 <= x) * (x <= d * 0.5),
    #                          (d * 0.5 < x) * (x < d * 1.5)
    #                      ],
    #                      [
    #                          lambda v: ((1.5 * d + v) ** 2) / (2 * (d ** 3)),
    #                          lambda v: 3.0 / (4.0 * d) - (v * v) / (d ** 3),
    #                          lambda v: ((1.5 * d - v) ** 2) / (2 * (d ** 3))
    #                      ])
    left_func = ((1.5 * d + x) ** 2) / (2 * (d ** 3))
    middle_func = 3.0 / (4.0 * d) - (x * x) / (d ** 3)
    right_func = ((1.5 * d - x) ** 2) / (2 * (d ** 3))
    value = left_func * ((- d * 1.5 < x) * (x < - d * 0.5)) \
            + middle_func * ((- d * 0.5 <= x) * (x <= d * 0.5)) \
            + right_func * ((d * 0.5 < x) * (x < d * 1.5))

    return value

def f(x, y):
    return __spline_smoothing_kernel(x, 1) * __spline_smoothing_kernel(y, 1)

for x in range(-6, 7):
    print(__spline_smoothing_kernel(x * 0.25, 1))