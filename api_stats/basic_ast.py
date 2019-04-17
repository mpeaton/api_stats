from ast import *
Module(
    body=[
        ImportFrom(
            lineno=7,
            col_offset=0,
            module='__future__',
            names=[
                alias(name='division', asname=None),
                alias(name='print_function', asname=None),
                alias(name='absolute_import', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=9,
            col_offset=0,
            module='warnings',
            names=[alias(name='warn', asname=None)],
            level=0,
        ),
        Import(
            lineno=10,
            col_offset=0,
            names=[alias(name='numpy', asname='np')],
        ),
        ImportFrom(
            lineno=11,
            col_offset=0,
            module='numpy',
            names=[
                alias(name='atleast_1d', asname=None),
                alias(name='atleast_2d', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=12,
            col_offset=0,
            module='flinalg',
            names=[alias(name='get_flinalg_funcs', asname=None)],
            level=1,
        ),
        ImportFrom(
            lineno=13,
            col_offset=0,
            module='lapack',
            names=[
                alias(name='get_lapack_funcs', asname=None),
                alias(name='_compute_lwork', asname=None),
            ],
            level=1,
        ),
        ImportFrom(
            lineno=14,
            col_offset=0,
            module='misc',
            names=[
                alias(name='LinAlgError', asname=None),
                alias(name='_datacopied', asname=None),
                alias(name='LinAlgWarning', asname=None),
            ],
            level=1,
        ),
        ImportFrom(
            lineno=15,
            col_offset=0,
            module='decomp',
            names=[alias(name='_asarray_validated', asname=None)],
            level=1,
        ),
        ImportFrom(
            lineno=16,
            col_offset=0,
            module=None,
            names=[
                alias(name='decomp', asname=None),
                alias(name='decomp_svd', asname=None),
            ],
            level=1,
        ),
        ImportFrom(
            lineno=17,
            col_offset=0,
            module='_solve_toeplitz',
            names=[alias(name='levinson', asname=None)],
            level=1,
        ),
        Assign(
            lineno=19,
            col_offset=0,
            targets=[Name(lineno=19, col_offset=0, id='__all__', ctx=Store())],
            value=List(
                lineno=19,
                col_offset=10,
                elts=[
                    Str(lineno=19, col_offset=11, s='solve'),
                    Str(lineno=19, col_offset=20, s='solve_triangular'),
                    Str(lineno=19, col_offset=40, s='solveh_banded'),
                    Str(lineno=19, col_offset=57, s='solve_banded'),
                    Str(lineno=20, col_offset=11, s='solve_toeplitz'),
                    Str(lineno=20, col_offset=29, s='solve_circulant'),
                    Str(lineno=20, col_offset=48, s='inv'),
                    Str(lineno=20, col_offset=55, s='det'),
                    Str(lineno=20, col_offset=62, s='lstsq'),
                    Str(lineno=21, col_offset=11, s='pinv'),
                    Str(lineno=21, col_offset=19, s='pinv2'),
                    Str(lineno=21, col_offset=28, s='pinvh'),
                    Str(lineno=21, col_offset=37, s='matrix_balance'),
                ],
                ctx=Load(),
            ),
        ),
        FunctionDef(
            lineno=25,
            col_offset=0,
            name='_solve_check',
            args=arguments(
                args=[
                    arg(lineno=25, col_offset=17, arg='n', annotation=None),
                    arg(lineno=25, col_offset=20, arg='info', annotation=None),
                    arg(lineno=25, col_offset=26, arg='lamch', annotation=None),
                    arg(lineno=25, col_offset=38, arg='rcond', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    NameConstant(lineno=25, col_offset=32, value=None),
                    NameConstant(lineno=25, col_offset=44, value=None),
                ],
            ),
            body=[
                Expr(
                    lineno=26,
                    col_offset=4,
                    value=Str(lineno=26, col_offset=4, s=' Check arguments during the different steps of the solution phase '),
                ),
                If(
                    lineno=27,
                    col_offset=4,
                    test=Compare(
                        lineno=27,
                        col_offset=7,
                        left=Name(lineno=27, col_offset=7, id='info', ctx=Load()),
                        ops=[Lt()],
                        comparators=[Num(lineno=27, col_offset=14, n=0)],
                    ),
                    body=[
                        Raise(
                            lineno=28,
                            col_offset=8,
                            exc=Call(
                                lineno=28,
                                col_offset=14,
                                func=Name(lineno=28, col_offset=14, id='ValueError', ctx=Load()),
                                args=[
                                    Call(
                                        lineno=28,
                                        col_offset=25,
                                        func=Attribute(
                                            lineno=28,
                                            col_offset=25,
                                            value=Str(lineno=28, col_offset=25, s='LAPACK reported an illegal value in {}-th argument.'),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            UnaryOp(
                                                lineno=29,
                                                col_offset=36,
                                                op=USub(),
                                                operand=Name(lineno=29, col_offset=37, id='info', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[
                        If(
                            lineno=30,
                            col_offset=9,
                            test=Compare(
                                lineno=30,
                                col_offset=9,
                                left=Num(lineno=30, col_offset=9, n=0),
                                ops=[Lt()],
                                comparators=[Name(lineno=30, col_offset=13, id='info', ctx=Load())],
                            ),
                            body=[
                                Raise(
                                    lineno=31,
                                    col_offset=8,
                                    exc=Call(
                                        lineno=31,
                                        col_offset=14,
                                        func=Name(lineno=31, col_offset=14, id='LinAlgError', ctx=Load()),
                                        args=[Str(lineno=31, col_offset=26, s='Matrix is singular.')],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                ),
                If(
                    lineno=33,
                    col_offset=4,
                    test=Compare(
                        lineno=33,
                        col_offset=7,
                        left=Name(lineno=33, col_offset=7, id='lamch', ctx=Load()),
                        ops=[Is()],
                        comparators=[NameConstant(lineno=33, col_offset=16, value=None)],
                    ),
                    body=[Return(lineno=34, col_offset=8, value=None)],
                    orelse=[],
                ),
                Assign(
                    lineno=35,
                    col_offset=4,
                    targets=[Name(lineno=35, col_offset=4, id='E', ctx=Store())],
                    value=Call(
                        lineno=35,
                        col_offset=8,
                        func=Name(lineno=35, col_offset=8, id='lamch', ctx=Load()),
                        args=[Str(lineno=35, col_offset=14, s='E')],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=36,
                    col_offset=4,
                    test=Compare(
                        lineno=36,
                        col_offset=7,
                        left=Name(lineno=36, col_offset=7, id='rcond', ctx=Load()),
                        ops=[Lt()],
                        comparators=[Name(lineno=36, col_offset=15, id='E', ctx=Load())],
                    ),
                    body=[
                        Expr(
                            lineno=37,
                            col_offset=8,
                            value=Call(
                                lineno=37,
                                col_offset=8,
                                func=Name(lineno=37, col_offset=8, id='warn', ctx=Load()),
                                args=[
                                    Call(
                                        lineno=37,
                                        col_offset=13,
                                        func=Attribute(
                                            lineno=37,
                                            col_offset=13,
                                            value=Str(lineno=37, col_offset=13, s='Ill-conditioned matrix (rcond={:.6g}): result may not be accurate.'),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=38, col_offset=50, id='rcond', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(lineno=39, col_offset=13, id='LinAlgWarning', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='stacklevel',
                                        value=Num(lineno=39, col_offset=39, n=3),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=42,
            col_offset=0,
            name='solve',
            args=arguments(
                args=[
                    arg(lineno=42, col_offset=10, arg='a', annotation=None),
                    arg(lineno=42, col_offset=13, arg='b', annotation=None),
                    arg(lineno=42, col_offset=16, arg='sym_pos', annotation=None),
                    arg(lineno=42, col_offset=31, arg='lower', annotation=None),
                    arg(lineno=42, col_offset=44, arg='overwrite_a', annotation=None),
                    arg(lineno=43, col_offset=10, arg='overwrite_b', annotation=None),
                    arg(lineno=43, col_offset=29, arg='debug', annotation=None),
                    arg(lineno=43, col_offset=41, arg='check_finite', annotation=None),
                    arg(lineno=43, col_offset=60, arg='assume_a', annotation=None),
                    arg(lineno=44, col_offset=10, arg='transposed', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    NameConstant(lineno=42, col_offset=24, value=False),
                    NameConstant(lineno=42, col_offset=37, value=False),
                    NameConstant(lineno=42, col_offset=56, value=False),
                    NameConstant(lineno=43, col_offset=22, value=False),
                    NameConstant(lineno=43, col_offset=35, value=None),
                    NameConstant(lineno=43, col_offset=54, value=True),
                    Str(lineno=43, col_offset=69, s='gen'),
                    NameConstant(lineno=44, col_offset=21, value=False),
                ],
            ),
            body=[
                Expr(
                    lineno=135,
                    col_offset=-1,
                    value=Str(lineno=135, col_offset=-1, s="\n    Solves the linear equation set ``a * x = b`` for the unknown ``x``\n    for square ``a`` matrix.\n\n    If the data matrix is known to be a particular type then supplying the\n    corresponding string to ``assume_a`` key chooses the dedicated solver.\n    The available options are\n\n    ===================  ========\n     generic matrix       'gen'\n     symmetric            'sym'\n     hermitian            'her'\n     positive definite    'pos'\n    ===================  ========\n\n    If omitted, ``'gen'`` is the default structure.\n\n    The datatype of the arrays define which solver is called regardless\n    of the values. In other words, even when the complex array entries have\n    precisely zero imaginary parts, the complex solver will be called based\n    on the data type of the array.\n\n    Parameters\n    ----------\n    a : (N, N) array_like\n        Square input data\n    b : (N, NRHS) array_like\n        Input data for the right hand side.\n    sym_pos : bool, optional\n        Assume `a` is symmetric and positive definite. This key is deprecated\n        and assume_a = 'pos' keyword is recommended instead. The functionality\n        is the same. It will be removed in the future.\n    lower : bool, optional\n        If True, only the data contained in the lower triangle of `a`. Default\n        is to use upper triangle. (ignored for ``'gen'``)\n    overwrite_a : bool, optional\n        Allow overwriting data in `a` (may enhance performance).\n        Default is False.\n    overwrite_b : bool, optional\n        Allow overwriting data in `b` (may enhance performance).\n        Default is False.\n    check_finite : bool, optional\n        Whether to check that the input matrices contain only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n    assume_a : str, optional\n        Valid entries are explained above.\n    transposed: bool, optional\n        If True, ``a^T x = b`` for real matrices, raises `NotImplementedError`\n        for complex matrices (only for True).\n\n    Returns\n    -------\n    x : (N, NRHS) ndarray\n        The solution array.\n\n    Raises\n    ------\n    ValueError\n        If size mismatches detected or input a is not square.\n    LinAlgError\n        If the matrix is singular.\n    LinAlgWarning\n        If an ill-conditioned input a is detected.\n    NotImplementedError\n        If transposed is True and input a is a complex matrix.\n\n    Examples\n    --------\n    Given `a` and `b`, solve for `x`:\n\n    >>> a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])\n    >>> b = np.array([2, 4, -1])\n    >>> from scipy import linalg\n    >>> x = linalg.solve(a, b)\n    >>> x\n    array([ 2., -2.,  9.])\n    >>> np.dot(a, x) == b\n    array([ True,  True,  True], dtype=bool)\n\n    Notes\n    -----\n    If the input b matrix is a 1D array with N elements, when supplied\n    together with an NxN input a, it is assumed as a valid column vector\n    despite the apparent size mismatch. This is compatible with the\n    numpy.dot() behavior and the returned result is still 1D array.\n\n    The generic, symmetric, hermitian and positive definite solutions are\n    obtained via calling ?GESV, ?SYSV, ?HESV, and ?POSV routines of\n    LAPACK respectively.\n    "),
                ),
                Assign(
                    lineno=137,
                    col_offset=4,
                    targets=[Name(lineno=137, col_offset=4, id='b_is_1D', ctx=Store())],
                    value=NameConstant(lineno=137, col_offset=14, value=False),
                ),
                Assign(
                    lineno=139,
                    col_offset=4,
                    targets=[Name(lineno=139, col_offset=4, id='a1', ctx=Store())],
                    value=Call(
                        lineno=139,
                        col_offset=9,
                        func=Name(lineno=139, col_offset=9, id='atleast_2d', ctx=Load()),
                        args=[
                            Call(
                                lineno=139,
                                col_offset=20,
                                func=Name(lineno=139, col_offset=20, id='_asarray_validated', ctx=Load()),
                                args=[Name(lineno=139, col_offset=39, id='a', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='check_finite',
                                        value=Name(lineno=139, col_offset=55, id='check_finite', ctx=Load()),
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=140,
                    col_offset=4,
                    targets=[Name(lineno=140, col_offset=4, id='b1', ctx=Store())],
                    value=Call(
                        lineno=140,
                        col_offset=9,
                        func=Name(lineno=140, col_offset=9, id='atleast_1d', ctx=Load()),
                        args=[
                            Call(
                                lineno=140,
                                col_offset=20,
                                func=Name(lineno=140, col_offset=20, id='_asarray_validated', ctx=Load()),
                                args=[Name(lineno=140, col_offset=39, id='b', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='check_finite',
                                        value=Name(lineno=140, col_offset=55, id='check_finite', ctx=Load()),
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=141,
                    col_offset=4,
                    targets=[Name(lineno=141, col_offset=4, id='n', ctx=Store())],
                    value=Subscript(
                        lineno=141,
                        col_offset=8,
                        value=Attribute(
                            lineno=141,
                            col_offset=8,
                            value=Name(lineno=141, col_offset=8, id='a1', ctx=Load()),
                            attr='shape',
                            ctx=Load(),
                        ),
                        slice=Index(
                            value=Num(lineno=141, col_offset=17, n=0),
                        ),
                        ctx=Load(),
                    ),
                ),
                Assign(
                    lineno=143,
                    col_offset=4,
                    targets=[Name(lineno=143, col_offset=4, id='overwrite_a', ctx=Store())],
                    value=BoolOp(
                        lineno=143,
                        col_offset=18,
                        op=Or(),
                        values=[
                            Name(lineno=143, col_offset=18, id='overwrite_a', ctx=Load()),
                            Call(
                                lineno=143,
                                col_offset=33,
                                func=Name(lineno=143, col_offset=33, id='_datacopied', ctx=Load()),
                                args=[
                                    Name(lineno=143, col_offset=45, id='a1', ctx=Load()),
                                    Name(lineno=143, col_offset=49, id='a', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=144,
                    col_offset=4,
                    targets=[Name(lineno=144, col_offset=4, id='overwrite_b', ctx=Store())],
                    value=BoolOp(
                        lineno=144,
                        col_offset=18,
                        op=Or(),
                        values=[
                            Name(lineno=144, col_offset=18, id='overwrite_b', ctx=Load()),
                            Call(
                                lineno=144,
                                col_offset=33,
                                func=Name(lineno=144, col_offset=33, id='_datacopied', ctx=Load()),
                                args=[
                                    Name(lineno=144, col_offset=45, id='b1', ctx=Load()),
                                    Name(lineno=144, col_offset=49, id='b', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=146,
                    col_offset=4,
                    test=Compare(
                        lineno=146,
                        col_offset=7,
                        left=Subscript(
                            lineno=146,
                            col_offset=7,
                            value=Attribute(
                                lineno=146,
                                col_offset=7,
                                value=Name(lineno=146, col_offset=7, id='a1', ctx=Load()),
                                attr='shape',
                                ctx=Load(),
                            ),
                            slice=Index(
                                value=Num(lineno=146, col_offset=16, n=0),
                            ),
                            ctx=Load(),
                        ),
                        ops=[NotEq()],
                        comparators=[
                            Subscript(
                                lineno=146,
                                col_offset=22,
                                value=Attribute(
                                    lineno=146,
                                    col_offset=22,
                                    value=Name(lineno=146, col_offset=22, id='a1', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                                slice=Index(
                                    value=Num(lineno=146, col_offset=31, n=1),
                                ),
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            lineno=147,
                            col_offset=8,
                            exc=Call(
                                lineno=147,
                                col_offset=14,
                                func=Name(lineno=147, col_offset=14, id='ValueError', ctx=Load()),
                                args=[Str(lineno=147, col_offset=25, s='Input a needs to be a square matrix.')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=149,
                    col_offset=4,
                    test=Compare(
                        lineno=149,
                        col_offset=7,
                        left=Name(lineno=149, col_offset=7, id='n', ctx=Load()),
                        ops=[NotEq()],
                        comparators=[
                            Subscript(
                                lineno=149,
                                col_offset=12,
                                value=Attribute(
                                    lineno=149,
                                    col_offset=12,
                                    value=Name(lineno=149, col_offset=12, id='b1', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                                slice=Index(
                                    value=Num(lineno=149, col_offset=21, n=0),
                                ),
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        If(
                            lineno=151,
                            col_offset=8,
                            test=UnaryOp(
                                lineno=151,
                                col_offset=11,
                                op=Not(),
                                operand=BoolOp(
                                    lineno=151,
                                    col_offset=16,
                                    op=And(),
                                    values=[
                                        Compare(
                                            lineno=151,
                                            col_offset=16,
                                            left=Name(lineno=151, col_offset=16, id='n', ctx=Load()),
                                            ops=[Eq()],
                                            comparators=[Num(lineno=151, col_offset=21, n=1)],
                                        ),
                                        Compare(
                                            lineno=151,
                                            col_offset=27,
                                            left=Attribute(
                                                lineno=151,
                                                col_offset=27,
                                                value=Name(lineno=151, col_offset=27, id='b1', ctx=Load()),
                                                attr='size',
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[Num(lineno=151, col_offset=38, n=0)],
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Raise(
                                    lineno=152,
                                    col_offset=12,
                                    exc=Call(
                                        lineno=152,
                                        col_offset=18,
                                        func=Name(lineno=152, col_offset=18, id='ValueError', ctx=Load()),
                                        args=[Str(lineno=152, col_offset=29, s='Input b has to have same number of rows as input a')],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=156,
                    col_offset=4,
                    test=Compare(
                        lineno=156,
                        col_offset=7,
                        left=Attribute(
                            lineno=156,
                            col_offset=7,
                            value=Name(lineno=156, col_offset=7, id='b1', ctx=Load()),
                            attr='size',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Num(lineno=156, col_offset=18, n=0)],
                    ),
                    body=[
                        Return(
                            lineno=157,
                            col_offset=8,
                            value=Call(
                                lineno=157,
                                col_offset=15,
                                func=Attribute(
                                    lineno=157,
                                    col_offset=15,
                                    value=Name(lineno=157, col_offset=15, id='np', ctx=Load()),
                                    attr='asfortranarray',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        lineno=157,
                                        col_offset=33,
                                        func=Attribute(
                                            lineno=157,
                                            col_offset=33,
                                            value=Name(lineno=157, col_offset=33, id='b1', ctx=Load()),
                                            attr='copy',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=160,
                    col_offset=4,
                    test=Compare(
                        lineno=160,
                        col_offset=7,
                        left=Attribute(
                            lineno=160,
                            col_offset=7,
                            value=Name(lineno=160, col_offset=7, id='b1', ctx=Load()),
                            attr='ndim',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Num(lineno=160, col_offset=18, n=1)],
                    ),
                    body=[
                        If(
                            lineno=161,
                            col_offset=8,
                            test=Compare(
                                lineno=161,
                                col_offset=11,
                                left=Name(lineno=161, col_offset=11, id='n', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Num(lineno=161, col_offset=16, n=1)],
                            ),
                            body=[
                                Assign(
                                    lineno=162,
                                    col_offset=12,
                                    targets=[Name(lineno=162, col_offset=12, id='b1', ctx=Store())],
                                    value=Subscript(
                                        lineno=162,
                                        col_offset=17,
                                        value=Name(lineno=162, col_offset=17, id='b1', ctx=Load()),
                                        slice=ExtSlice(
                                            dims=[
                                                Index(
                                                    value=NameConstant(lineno=162, col_offset=20, value=None),
                                                ),
                                                Slice(lower=None, upper=None, step=None),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    lineno=164,
                                    col_offset=12,
                                    targets=[Name(lineno=164, col_offset=12, id='b1', ctx=Store())],
                                    value=Subscript(
                                        lineno=164,
                                        col_offset=17,
                                        value=Name(lineno=164, col_offset=17, id='b1', ctx=Load()),
                                        slice=ExtSlice(
                                            dims=[
                                                Slice(lower=None, upper=None, step=None),
                                                Index(
                                                    value=NameConstant(lineno=164, col_offset=23, value=None),
                                                ),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                        Assign(
                            lineno=165,
                            col_offset=8,
                            targets=[Name(lineno=165, col_offset=8, id='b_is_1D', ctx=Store())],
                            value=NameConstant(lineno=165, col_offset=18, value=True),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=168,
                    col_offset=4,
                    test=Name(lineno=168, col_offset=7, id='sym_pos', ctx=Load()),
                    body=[
                        Assign(
                            lineno=169,
                            col_offset=8,
                            targets=[Name(lineno=169, col_offset=8, id='assume_a', ctx=Store())],
                            value=Str(lineno=169, col_offset=19, s='pos'),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=171,
                    col_offset=4,
                    test=Compare(
                        lineno=171,
                        col_offset=7,
                        left=Name(lineno=171, col_offset=7, id='assume_a', ctx=Load()),
                        ops=[NotIn()],
                        comparators=[
                            Tuple(
                                lineno=171,
                                col_offset=24,
                                elts=[
                                    Str(lineno=171, col_offset=24, s='gen'),
                                    Str(lineno=171, col_offset=31, s='sym'),
                                    Str(lineno=171, col_offset=38, s='her'),
                                    Str(lineno=171, col_offset=45, s='pos'),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            lineno=172,
                            col_offset=8,
                            exc=Call(
                                lineno=172,
                                col_offset=14,
                                func=Name(lineno=172, col_offset=14, id='ValueError', ctx=Load()),
                                args=[
                                    Call(
                                        lineno=172,
                                        col_offset=25,
                                        func=Attribute(
                                            lineno=172,
                                            col_offset=25,
                                            value=Str(lineno=172, col_offset=25, s='{} is not a recognized matrix structure'),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=173, col_offset=35, id='assume_a', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=176,
                    col_offset=4,
                    test=Compare(
                        lineno=176,
                        col_offset=7,
                        left=Name(lineno=176, col_offset=7, id='debug', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[NameConstant(lineno=176, col_offset=20, value=None)],
                    ),
                    body=[
                        Expr(
                            lineno=177,
                            col_offset=8,
                            value=Call(
                                lineno=177,
                                col_offset=8,
                                func=Name(lineno=177, col_offset=8, id='warn', ctx=Load()),
                                args=[
                                    Str(lineno=177, col_offset=13, s='Use of the "debug" keyword is deprecated and this keyword will be removed in future versions of SciPy.'),
                                    Name(lineno=179, col_offset=35, id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='stacklevel',
                                        value=Num(lineno=179, col_offset=66, n=2),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=184,
                    col_offset=4,
                    test=Compare(
                        lineno=184,
                        col_offset=7,
                        left=Attribute(
                            lineno=184,
                            col_offset=7,
                            value=Attribute(
                                lineno=184,
                                col_offset=7,
                                value=Name(lineno=184, col_offset=7, id='a1', ctx=Load()),
                                attr='dtype',
                                ctx=Load(),
                            ),
                            attr='char',
                            ctx=Load(),
                        ),
                        ops=[In()],
                        comparators=[Str(lineno=184, col_offset=24, s='fF')],
                    ),
                    body=[
                        Assign(
                            lineno=185,
                            col_offset=8,
                            targets=[Name(lineno=185, col_offset=8, id='lamch', ctx=Store())],
                            value=Call(
                                lineno=185,
                                col_offset=16,
                                func=Name(lineno=185, col_offset=16, id='get_lapack_funcs', ctx=Load()),
                                args=[Str(lineno=185, col_offset=33, s='lamch')],
                                keywords=[
                                    keyword(
                                        arg='dtype',
                                        value=Str(lineno=185, col_offset=48, s='f'),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[
                        Assign(
                            lineno=187,
                            col_offset=8,
                            targets=[Name(lineno=187, col_offset=8, id='lamch', ctx=Store())],
                            value=Call(
                                lineno=187,
                                col_offset=16,
                                func=Name(lineno=187, col_offset=16, id='get_lapack_funcs', ctx=Load()),
                                args=[Str(lineno=187, col_offset=33, s='lamch')],
                                keywords=[
                                    keyword(
                                        arg='dtype',
                                        value=Str(lineno=187, col_offset=48, s='d'),
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                Assign(
                    lineno=192,
                    col_offset=4,
                    targets=[Name(lineno=192, col_offset=4, id='lange', ctx=Store())],
                    value=Call(
                        lineno=192,
                        col_offset=12,
                        func=Name(lineno=192, col_offset=12, id='get_lapack_funcs', ctx=Load()),
                        args=[
                            Str(lineno=192, col_offset=29, s='lange'),
                            Tuple(
                                lineno=192,
                                col_offset=39,
                                elts=[Name(lineno=192, col_offset=39, id='a1', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=198,
                    col_offset=4,
                    test=Name(lineno=198, col_offset=7, id='transposed', ctx=Load()),
                    body=[
                        Assign(
                            lineno=199,
                            col_offset=8,
                            targets=[Name(lineno=199, col_offset=8, id='trans', ctx=Store())],
                            value=Num(lineno=199, col_offset=16, n=1),
                        ),
                        Assign(
                            lineno=200,
                            col_offset=8,
                            targets=[Name(lineno=200, col_offset=8, id='norm', ctx=Store())],
                            value=Str(lineno=200, col_offset=15, s='I'),
                        ),
                        If(
                            lineno=201,
                            col_offset=8,
                            test=Call(
                                lineno=201,
                                col_offset=11,
                                func=Attribute(
                                    lineno=201,
                                    col_offset=11,
                                    value=Name(lineno=201, col_offset=11, id='np', ctx=Load()),
                                    attr='iscomplexobj',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=201, col_offset=27, id='a1', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    lineno=202,
                                    col_offset=12,
                                    exc=Call(
                                        lineno=202,
                                        col_offset=18,
                                        func=Name(lineno=202, col_offset=18, id='NotImplementedError', ctx=Load()),
                                        args=[Str(lineno=202, col_offset=38, s='scipy.linalg.solve can currently not solve a^T x = b or a^H x = b for complex matrices.')],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[
                        Assign(
                            lineno=206,
                            col_offset=8,
                            targets=[Name(lineno=206, col_offset=8, id='trans', ctx=Store())],
                            value=Num(lineno=206, col_offset=16, n=0),
                        ),
                        Assign(
                            lineno=207,
                            col_offset=8,
                            targets=[Name(lineno=207, col_offset=8, id='norm', ctx=Store())],
                            value=Str(lineno=207, col_offset=15, s='1'),
                        ),
                    ],
                ),
                Assign(
                    lineno=209,
                    col_offset=4,
                    targets=[Name(lineno=209, col_offset=4, id='anorm', ctx=Store())],
                    value=Call(
                        lineno=209,
                        col_offset=12,
                        func=Name(lineno=209, col_offset=12, id='lange', ctx=Load()),
                        args=[
                            Name(lineno=209, col_offset=18, id='norm', ctx=Load()),
                            Name(lineno=209, col_offset=24, id='a1', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=212,
                    col_offset=4,
                    test=Compare(
                        lineno=212,
                        col_offset=7,
                        left=Name(lineno=212, col_offset=7, id='assume_a', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Str(lineno=212, col_offset=19, s='gen')],
                    ),
                    body=[
                        Assign(
                            lineno=213,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=213,
                                    col_offset=8,
                                    elts=[
                                        Name(lineno=213, col_offset=8, id='gecon', ctx=Store()),
                                        Name(lineno=213, col_offset=15, id='getrf', ctx=Store()),
                                        Name(lineno=213, col_offset=22, id='getrs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=213,
                                col_offset=30,
                                func=Name(lineno=213, col_offset=30, id='get_lapack_funcs', ctx=Load()),
                                args=[
                                    Tuple(
                                        lineno=213,
                                        col_offset=48,
                                        elts=[
                                            Str(lineno=213, col_offset=48, s='gecon'),
                                            Str(lineno=213, col_offset=57, s='getrf'),
                                            Str(lineno=213, col_offset=66, s='getrs'),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=214,
                                        col_offset=48,
                                        elts=[
                                            Name(lineno=214, col_offset=48, id='a1', ctx=Load()),
                                            Name(lineno=214, col_offset=52, id='b1', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=215,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=215,
                                    col_offset=8,
                                    elts=[
                                        Name(lineno=215, col_offset=8, id='lu', ctx=Store()),
                                        Name(lineno=215, col_offset=12, id='ipvt', ctx=Store()),
                                        Name(lineno=215, col_offset=18, id='info', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=215,
                                col_offset=25,
                                func=Name(lineno=215, col_offset=25, id='getrf', ctx=Load()),
                                args=[Name(lineno=215, col_offset=31, id='a1', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='overwrite_a',
                                        value=Name(lineno=215, col_offset=47, id='overwrite_a', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            lineno=216,
                            col_offset=8,
                            value=Call(
                                lineno=216,
                                col_offset=8,
                                func=Name(lineno=216, col_offset=8, id='_solve_check', ctx=Load()),
                                args=[
                                    Name(lineno=216, col_offset=21, id='n', ctx=Load()),
                                    Name(lineno=216, col_offset=24, id='info', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=217,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=217,
                                    col_offset=8,
                                    elts=[
                                        Name(lineno=217, col_offset=8, id='x', ctx=Store()),
                                        Name(lineno=217, col_offset=11, id='info', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=217,
                                col_offset=18,
                                func=Name(lineno=217, col_offset=18, id='getrs', ctx=Load()),
                                args=[
                                    Name(lineno=217, col_offset=24, id='lu', ctx=Load()),
                                    Name(lineno=217, col_offset=28, id='ipvt', ctx=Load()),
                                    Name(lineno=217, col_offset=34, id='b1', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='trans',
                                        value=Name(lineno=218, col_offset=30, id='trans', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='overwrite_b',
                                        value=Name(lineno=218, col_offset=49, id='overwrite_b', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            lineno=219,
                            col_offset=8,
                            value=Call(
                                lineno=219,
                                col_offset=8,
                                func=Name(lineno=219, col_offset=8, id='_solve_check', ctx=Load()),
                                args=[
                                    Name(lineno=219, col_offset=21, id='n', ctx=Load()),
                                    Name(lineno=219, col_offset=24, id='info', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=220,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=220,
                                    col_offset=8,
                                    elts=[
                                        Name(lineno=220, col_offset=8, id='rcond', ctx=Store()),
                                        Name(lineno=220, col_offset=15, id='info', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=220,
                                col_offset=22,
                                func=Name(lineno=220, col_offset=22, id='gecon', ctx=Load()),
                                args=[
                                    Name(lineno=220, col_offset=28, id='lu', ctx=Load()),
                                    Name(lineno=220, col_offset=32, id='anorm', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='norm',
                                        value=Name(lineno=220, col_offset=44, id='norm', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[
                        If(
                            lineno=222,
                            col_offset=9,
                            test=Compare(
                                lineno=222,
                                col_offset=9,
                                left=Name(lineno=222, col_offset=9, id='assume_a', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Str(lineno=222, col_offset=21, s='her')],
                            ),
                            body=[
                                Assign(
                                    lineno=223,
                                    col_offset=8,
                                    targets=[
                                        Tuple(
                                            lineno=223,
                                            col_offset=8,
                                            elts=[
                                                Name(lineno=223, col_offset=8, id='hecon', ctx=Store()),
                                                Name(lineno=223, col_offset=15, id='hesv', ctx=Store()),
                                                Name(lineno=223, col_offset=21, id='hesv_lw', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=223,
                                        col_offset=31,
                                        func=Name(lineno=223, col_offset=31, id='get_lapack_funcs', ctx=Load()),
                                        args=[
                                            Tuple(
                                                lineno=223,
                                                col_offset=49,
                                                elts=[
                                                    Str(lineno=223, col_offset=49, s='hecon'),
                                                    Str(lineno=223, col_offset=58, s='hesv'),
                                                    Str(lineno=224, col_offset=49, s='hesv_lwork'),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                lineno=224,
                                                col_offset=65,
                                                elts=[
                                                    Name(lineno=224, col_offset=65, id='a1', ctx=Load()),
                                                    Name(lineno=224, col_offset=69, id='b1', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    lineno=225,
                                    col_offset=8,
                                    targets=[Name(lineno=225, col_offset=8, id='lwork', ctx=Store())],
                                    value=Call(
                                        lineno=225,
                                        col_offset=16,
                                        func=Name(lineno=225, col_offset=16, id='_compute_lwork', ctx=Load()),
                                        args=[
                                            Name(lineno=225, col_offset=31, id='hesv_lw', ctx=Load()),
                                            Name(lineno=225, col_offset=40, id='n', ctx=Load()),
                                            Name(lineno=225, col_offset=43, id='lower', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    lineno=226,
                                    col_offset=8,
                                    targets=[
                                        Tuple(
                                            lineno=226,
                                            col_offset=8,
                                            elts=[
                                                Name(lineno=226, col_offset=8, id='lu', ctx=Store()),
                                                Name(lineno=226, col_offset=12, id='ipvt', ctx=Store()),
                                                Name(lineno=226, col_offset=18, id='x', ctx=Store()),
                                                Name(lineno=226, col_offset=21, id='info', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=226,
                                        col_offset=28,
                                        func=Name(lineno=226, col_offset=28, id='hesv', ctx=Load()),
                                        args=[
                                            Name(lineno=226, col_offset=33, id='a1', ctx=Load()),
                                            Name(lineno=226, col_offset=37, id='b1', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='lwork',
                                                value=Name(lineno=226, col_offset=47, id='lwork', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='lower',
                                                value=Name(lineno=227, col_offset=39, id='lower', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='overwrite_a',
                                                value=Name(lineno=228, col_offset=45, id='overwrite_a', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='overwrite_b',
                                                value=Name(lineno=229, col_offset=45, id='overwrite_b', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    lineno=230,
                                    col_offset=8,
                                    value=Call(
                                        lineno=230,
                                        col_offset=8,
                                        func=Name(lineno=230, col_offset=8, id='_solve_check', ctx=Load()),
                                        args=[
                                            Name(lineno=230, col_offset=21, id='n', ctx=Load()),
                                            Name(lineno=230, col_offset=24, id='info', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    lineno=231,
                                    col_offset=8,
                                    targets=[
                                        Tuple(
                                            lineno=231,
                                            col_offset=8,
                                            elts=[
                                                Name(lineno=231, col_offset=8, id='rcond', ctx=Store()),
                                                Name(lineno=231, col_offset=15, id='info', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=231,
                                        col_offset=22,
                                        func=Name(lineno=231, col_offset=22, id='hecon', ctx=Load()),
                                        args=[
                                            Name(lineno=231, col_offset=28, id='lu', ctx=Load()),
                                            Name(lineno=231, col_offset=32, id='ipvt', ctx=Load()),
                                            Name(lineno=231, col_offset=38, id='anorm', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    lineno=233,
                                    col_offset=9,
                                    test=Compare(
                                        lineno=233,
                                        col_offset=9,
                                        left=Name(lineno=233, col_offset=9, id='assume_a', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Str(lineno=233, col_offset=21, s='sym')],
                                    ),
                                    body=[
                                        Assign(
                                            lineno=234,
                                            col_offset=8,
                                            targets=[
                                                Tuple(
                                                    lineno=234,
                                                    col_offset=8,
                                                    elts=[
                                                        Name(lineno=234, col_offset=8, id='sycon', ctx=Store()),
                                                        Name(lineno=234, col_offset=15, id='sysv', ctx=Store()),
                                                        Name(lineno=234, col_offset=21, id='sysv_lw', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                lineno=234,
                                                col_offset=31,
                                                func=Name(lineno=234, col_offset=31, id='get_lapack_funcs', ctx=Load()),
                                                args=[
                                                    Tuple(
                                                        lineno=234,
                                                        col_offset=49,
                                                        elts=[
                                                            Str(lineno=234, col_offset=49, s='sycon'),
                                                            Str(lineno=234, col_offset=58, s='sysv'),
                                                            Str(lineno=235, col_offset=49, s='sysv_lwork'),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        lineno=235,
                                                        col_offset=65,
                                                        elts=[
                                                            Name(lineno=235, col_offset=65, id='a1', ctx=Load()),
                                                            Name(lineno=235, col_offset=69, id='b1', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            lineno=236,
                                            col_offset=8,
                                            targets=[Name(lineno=236, col_offset=8, id='lwork', ctx=Store())],
                                            value=Call(
                                                lineno=236,
                                                col_offset=16,
                                                func=Name(lineno=236, col_offset=16, id='_compute_lwork', ctx=Load()),
                                                args=[
                                                    Name(lineno=236, col_offset=31, id='sysv_lw', ctx=Load()),
                                                    Name(lineno=236, col_offset=40, id='n', ctx=Load()),
                                                    Name(lineno=236, col_offset=43, id='lower', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            lineno=237,
                                            col_offset=8,
                                            targets=[
                                                Tuple(
                                                    lineno=237,
                                                    col_offset=8,
                                                    elts=[
                                                        Name(lineno=237, col_offset=8, id='lu', ctx=Store()),
                                                        Name(lineno=237, col_offset=12, id='ipvt', ctx=Store()),
                                                        Name(lineno=237, col_offset=18, id='x', ctx=Store()),
                                                        Name(lineno=237, col_offset=21, id='info', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                lineno=237,
                                                col_offset=28,
                                                func=Name(lineno=237, col_offset=28, id='sysv', ctx=Load()),
                                                args=[
                                                    Name(lineno=237, col_offset=33, id='a1', ctx=Load()),
                                                    Name(lineno=237, col_offset=37, id='b1', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='lwork',
                                                        value=Name(lineno=237, col_offset=47, id='lwork', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='lower',
                                                        value=Name(lineno=238, col_offset=39, id='lower', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='overwrite_a',
                                                        value=Name(lineno=239, col_offset=45, id='overwrite_a', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='overwrite_b',
                                                        value=Name(lineno=240, col_offset=45, id='overwrite_b', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            lineno=241,
                                            col_offset=8,
                                            value=Call(
                                                lineno=241,
                                                col_offset=8,
                                                func=Name(lineno=241, col_offset=8, id='_solve_check', ctx=Load()),
                                                args=[
                                                    Name(lineno=241, col_offset=21, id='n', ctx=Load()),
                                                    Name(lineno=241, col_offset=24, id='info', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            lineno=242,
                                            col_offset=8,
                                            targets=[
                                                Tuple(
                                                    lineno=242,
                                                    col_offset=8,
                                                    elts=[
                                                        Name(lineno=242, col_offset=8, id='rcond', ctx=Store()),
                                                        Name(lineno=242, col_offset=15, id='info', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                lineno=242,
                                                col_offset=22,
                                                func=Name(lineno=242, col_offset=22, id='sycon', ctx=Load()),
                                                args=[
                                                    Name(lineno=242, col_offset=28, id='lu', ctx=Load()),
                                                    Name(lineno=242, col_offset=32, id='ipvt', ctx=Load()),
                                                    Name(lineno=242, col_offset=38, id='anorm', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            lineno=245,
                                            col_offset=8,
                                            targets=[
                                                Tuple(
                                                    lineno=245,
                                                    col_offset=8,
                                                    elts=[
                                                        Name(lineno=245, col_offset=8, id='pocon', ctx=Store()),
                                                        Name(lineno=245, col_offset=15, id='posv', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                lineno=245,
                                                col_offset=22,
                                                func=Name(lineno=245, col_offset=22, id='get_lapack_funcs', ctx=Load()),
                                                args=[
                                                    Tuple(
                                                        lineno=245,
                                                        col_offset=40,
                                                        elts=[
                                                            Str(lineno=245, col_offset=40, s='pocon'),
                                                            Str(lineno=245, col_offset=49, s='posv'),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        lineno=246,
                                                        col_offset=40,
                                                        elts=[
                                                            Name(lineno=246, col_offset=40, id='a1', ctx=Load()),
                                                            Name(lineno=246, col_offset=44, id='b1', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            lineno=247,
                                            col_offset=8,
                                            targets=[
                                                Tuple(
                                                    lineno=247,
                                                    col_offset=8,
                                                    elts=[
                                                        Name(lineno=247, col_offset=8, id='lu', ctx=Store()),
                                                        Name(lineno=247, col_offset=12, id='x', ctx=Store()),
                                                        Name(lineno=247, col_offset=15, id='info', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                lineno=247,
                                                col_offset=22,
                                                func=Name(lineno=247, col_offset=22, id='posv', ctx=Load()),
                                                args=[
                                                    Name(lineno=247, col_offset=27, id='a1', ctx=Load()),
                                                    Name(lineno=247, col_offset=31, id='b1', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='lower',
                                                        value=Name(lineno=247, col_offset=41, id='lower', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='overwrite_a',
                                                        value=Name(lineno=248, col_offset=39, id='overwrite_a', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='overwrite_b',
                                                        value=Name(lineno=249, col_offset=39, id='overwrite_b', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            lineno=250,
                                            col_offset=8,
                                            value=Call(
                                                lineno=250,
                                                col_offset=8,
                                                func=Name(lineno=250, col_offset=8, id='_solve_check', ctx=Load()),
                                                args=[
                                                    Name(lineno=250, col_offset=21, id='n', ctx=Load()),
                                                    Name(lineno=250, col_offset=24, id='info', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            lineno=251,
                                            col_offset=8,
                                            targets=[
                                                Tuple(
                                                    lineno=251,
                                                    col_offset=8,
                                                    elts=[
                                                        Name(lineno=251, col_offset=8, id='rcond', ctx=Store()),
                                                        Name(lineno=251, col_offset=15, id='info', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                lineno=251,
                                                col_offset=22,
                                                func=Name(lineno=251, col_offset=22, id='pocon', ctx=Load()),
                                                args=[
                                                    Name(lineno=251, col_offset=28, id='lu', ctx=Load()),
                                                    Name(lineno=251, col_offset=32, id='anorm', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                Expr(
                    lineno=253,
                    col_offset=4,
                    value=Call(
                        lineno=253,
                        col_offset=4,
                        func=Name(lineno=253, col_offset=4, id='_solve_check', ctx=Load()),
                        args=[
                            Name(lineno=253, col_offset=17, id='n', ctx=Load()),
                            Name(lineno=253, col_offset=20, id='info', ctx=Load()),
                            Name(lineno=253, col_offset=26, id='lamch', ctx=Load()),
                            Name(lineno=253, col_offset=33, id='rcond', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=255,
                    col_offset=4,
                    test=Name(lineno=255, col_offset=7, id='b_is_1D', ctx=Load()),
                    body=[
                        Assign(
                            lineno=256,
                            col_offset=8,
                            targets=[Name(lineno=256, col_offset=8, id='x', ctx=Store())],
                            value=Call(
                                lineno=256,
                                col_offset=12,
                                func=Attribute(
                                    lineno=256,
                                    col_offset=12,
                                    value=Name(lineno=256, col_offset=12, id='x', ctx=Load()),
                                    attr='ravel',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    lineno=258,
                    col_offset=4,
                    value=Name(lineno=258, col_offset=11, id='x', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=261,
            col_offset=0,
            name='solve_triangular',
            args=arguments(
                args=[
                    arg(lineno=261, col_offset=21, arg='a', annotation=None),
                    arg(lineno=261, col_offset=24, arg='b', annotation=None),
                    arg(lineno=261, col_offset=27, arg='trans', annotation=None),
                    arg(lineno=261, col_offset=36, arg='lower', annotation=None),
                    arg(lineno=261, col_offset=49, arg='unit_diagonal', annotation=None),
                    arg(lineno=262, col_offset=21, arg='overwrite_b', annotation=None),
                    arg(lineno=262, col_offset=40, arg='debug', annotation=None),
                    arg(lineno=262, col_offset=52, arg='check_finite', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Num(lineno=261, col_offset=33, n=0),
                    NameConstant(lineno=261, col_offset=42, value=False),
                    NameConstant(lineno=261, col_offset=63, value=False),
                    NameConstant(lineno=262, col_offset=33, value=False),
                    NameConstant(lineno=262, col_offset=46, value=None),
                    NameConstant(lineno=262, col_offset=65, value=True),
                ],
            ),
            body=[
                Expr(
                    lineno=327,
                    col_offset=-1,
                    value=Str(lineno=327, col_offset=-1, s="\n    Solve the equation `a x = b` for `x`, assuming a is a triangular matrix.\n\n    Parameters\n    ----------\n    a : (M, M) array_like\n        A triangular matrix\n    b : (M,) or (M, N) array_like\n        Right-hand side matrix in `a x = b`\n    lower : bool, optional\n        Use only data contained in the lower triangle of `a`.\n        Default is to use upper triangle.\n    trans : {0, 1, 2, 'N', 'T', 'C'}, optional\n        Type of system to solve:\n\n        ========  =========\n        trans     system\n        ========  =========\n        0 or 'N'  a x  = b\n        1 or 'T'  a^T x = b\n        2 or 'C'  a^H x = b\n        ========  =========\n    unit_diagonal : bool, optional\n        If True, diagonal elements of `a` are assumed to be 1 and\n        will not be referenced.\n    overwrite_b : bool, optional\n        Allow overwriting data in `b` (may enhance performance)\n    check_finite : bool, optional\n        Whether to check that the input matrices contain only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n\n    Returns\n    -------\n    x : (M,) or (M, N) ndarray\n        Solution to the system `a x = b`.  Shape of return matches `b`.\n\n    Raises\n    ------\n    LinAlgError\n        If `a` is singular\n\n    Notes\n    -----\n    .. versionadded:: 0.9.0\n\n    Examples\n    --------\n    Solve the lower triangular system a x = b, where::\n\n             [3  0  0  0]       [4]\n        a =  [2  1  0  0]   b = [2]\n             [1  0  1  0]       [4]\n             [1  1  1  1]       [2]\n\n    >>> from scipy.linalg import solve_triangular\n    >>> a = np.array([[3, 0, 0, 0], [2, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])\n    >>> b = np.array([4, 2, 4, 2])\n    >>> x = solve_triangular(a, b, lower=True)\n    >>> x\n    array([ 1.33333333, -0.66666667,  2.66666667, -1.33333333])\n    >>> a.dot(x)  # Check the result\n    array([ 4.,  2.,  4.,  2.])\n\n    "),
                ),
                If(
                    lineno=330,
                    col_offset=4,
                    test=Compare(
                        lineno=330,
                        col_offset=7,
                        left=Name(lineno=330, col_offset=7, id='debug', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[NameConstant(lineno=330, col_offset=20, value=None)],
                    ),
                    body=[
                        Expr(
                            lineno=331,
                            col_offset=8,
                            value=Call(
                                lineno=331,
                                col_offset=8,
                                func=Name(lineno=331, col_offset=8, id='warn', ctx=Load()),
                                args=[
                                    Str(lineno=331, col_offset=13, s='Use of the "debug" keyword is deprecated and this keyword will be removed in the future versions of SciPy.'),
                                    Name(lineno=333, col_offset=35, id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='stacklevel',
                                        value=Num(lineno=333, col_offset=66, n=2),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=335,
                    col_offset=4,
                    targets=[Name(lineno=335, col_offset=4, id='a1', ctx=Store())],
                    value=Call(
                        lineno=335,
                        col_offset=9,
                        func=Name(lineno=335, col_offset=9, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=335, col_offset=28, id='a', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=335, col_offset=44, id='check_finite', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=336,
                    col_offset=4,
                    targets=[Name(lineno=336, col_offset=4, id='b1', ctx=Store())],
                    value=Call(
                        lineno=336,
                        col_offset=9,
                        func=Name(lineno=336, col_offset=9, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=336, col_offset=28, id='b', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=336, col_offset=44, id='check_finite', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=337,
                    col_offset=4,
                    test=BoolOp(
                        lineno=337,
                        col_offset=7,
                        op=Or(),
                        values=[
                            Compare(
                                lineno=337,
                                col_offset=7,
                                left=Call(
                                    lineno=337,
                                    col_offset=7,
                                    func=Name(lineno=337, col_offset=7, id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            lineno=337,
                                            col_offset=11,
                                            value=Name(lineno=337, col_offset=11, id='a1', ctx=Load()),
                                            attr='shape',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Num(lineno=337, col_offset=24, n=2)],
                            ),
                            Compare(
                                lineno=337,
                                col_offset=29,
                                left=Subscript(
                                    lineno=337,
                                    col_offset=29,
                                    value=Attribute(
                                        lineno=337,
                                        col_offset=29,
                                        value=Name(lineno=337, col_offset=29, id='a1', ctx=Load()),
                                        attr='shape',
                                        ctx=Load(),
                                    ),
                                    slice=Index(
                                        value=Num(lineno=337, col_offset=38, n=0),
                                    ),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Subscript(
                                        lineno=337,
                                        col_offset=44,
                                        value=Attribute(
                                            lineno=337,
                                            col_offset=44,
                                            value=Name(lineno=337, col_offset=44, id='a1', ctx=Load()),
                                            attr='shape',
                                            ctx=Load(),
                                        ),
                                        slice=Index(
                                            value=Num(lineno=337, col_offset=53, n=1),
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            lineno=338,
                            col_offset=8,
                            exc=Call(
                                lineno=338,
                                col_offset=14,
                                func=Name(lineno=338, col_offset=14, id='ValueError', ctx=Load()),
                                args=[Str(lineno=338, col_offset=25, s='expected square matrix')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=339,
                    col_offset=4,
                    test=Compare(
                        lineno=339,
                        col_offset=7,
                        left=Subscript(
                            lineno=339,
                            col_offset=7,
                            value=Attribute(
                                lineno=339,
                                col_offset=7,
                                value=Name(lineno=339, col_offset=7, id='a1', ctx=Load()),
                                attr='shape',
                                ctx=Load(),
                            ),
                            slice=Index(
                                value=Num(lineno=339, col_offset=16, n=0),
                            ),
                            ctx=Load(),
                        ),
                        ops=[NotEq()],
                        comparators=[
                            Subscript(
                                lineno=339,
                                col_offset=22,
                                value=Attribute(
                                    lineno=339,
                                    col_offset=22,
                                    value=Name(lineno=339, col_offset=22, id='b1', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                                slice=Index(
                                    value=Num(lineno=339, col_offset=31, n=0),
                                ),
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            lineno=340,
                            col_offset=8,
                            exc=Call(
                                lineno=340,
                                col_offset=14,
                                func=Name(lineno=340, col_offset=14, id='ValueError', ctx=Load()),
                                args=[Str(lineno=340, col_offset=25, s='incompatible dimensions')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=341,
                    col_offset=4,
                    targets=[Name(lineno=341, col_offset=4, id='overwrite_b', ctx=Store())],
                    value=BoolOp(
                        lineno=341,
                        col_offset=18,
                        op=Or(),
                        values=[
                            Name(lineno=341, col_offset=18, id='overwrite_b', ctx=Load()),
                            Call(
                                lineno=341,
                                col_offset=33,
                                func=Name(lineno=341, col_offset=33, id='_datacopied', ctx=Load()),
                                args=[
                                    Name(lineno=341, col_offset=45, id='b1', ctx=Load()),
                                    Name(lineno=341, col_offset=49, id='b', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=342,
                    col_offset=4,
                    test=Name(lineno=342, col_offset=7, id='debug', ctx=Load()),
                    body=[
                        Expr(
                            lineno=343,
                            col_offset=8,
                            value=Call(
                                lineno=343,
                                col_offset=8,
                                func=Name(lineno=343, col_offset=8, id='print', ctx=Load()),
                                args=[
                                    Str(lineno=343, col_offset=14, s='solve:overwrite_b='),
                                    Name(lineno=343, col_offset=36, id='overwrite_b', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=344,
                    col_offset=4,
                    targets=[Name(lineno=344, col_offset=4, id='trans', ctx=Store())],
                    value=Call(
                        lineno=344,
                        col_offset=12,
                        func=Attribute(
                            lineno=344,
                            col_offset=12,
                            value=Dict(
                                lineno=344,
                                col_offset=12,
                                keys=[
                                    Str(lineno=344, col_offset=13, s='N'),
                                    Str(lineno=344, col_offset=21, s='T'),
                                    Str(lineno=344, col_offset=29, s='C'),
                                ],
                                values=[
                                    Num(lineno=344, col_offset=18, n=0),
                                    Num(lineno=344, col_offset=26, n=1),
                                    Num(lineno=344, col_offset=34, n=2),
                                ],
                            ),
                            attr='get',
                            ctx=Load(),
                        ),
                        args=[
                            Name(lineno=344, col_offset=41, id='trans', ctx=Load()),
                            Name(lineno=344, col_offset=48, id='trans', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=345,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=345,
                            col_offset=4,
                            elts=[Name(lineno=345, col_offset=4, id='trtrs', ctx=Store())],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        lineno=345,
                        col_offset=13,
                        func=Name(lineno=345, col_offset=13, id='get_lapack_funcs', ctx=Load()),
                        args=[
                            Tuple(
                                lineno=345,
                                col_offset=31,
                                elts=[Str(lineno=345, col_offset=31, s='trtrs')],
                                ctx=Load(),
                            ),
                            Tuple(
                                lineno=345,
                                col_offset=43,
                                elts=[
                                    Name(lineno=345, col_offset=43, id='a1', ctx=Load()),
                                    Name(lineno=345, col_offset=47, id='b1', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=346,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=346,
                            col_offset=4,
                            elts=[
                                Name(lineno=346, col_offset=4, id='x', ctx=Store()),
                                Name(lineno=346, col_offset=7, id='info', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        lineno=346,
                        col_offset=14,
                        func=Name(lineno=346, col_offset=14, id='trtrs', ctx=Load()),
                        args=[
                            Name(lineno=346, col_offset=20, id='a1', ctx=Load()),
                            Name(lineno=346, col_offset=24, id='b1', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg='overwrite_b',
                                value=Name(lineno=346, col_offset=40, id='overwrite_b', ctx=Load()),
                            ),
                            keyword(
                                arg='lower',
                                value=Name(lineno=346, col_offset=59, id='lower', ctx=Load()),
                            ),
                            keyword(
                                arg='trans',
                                value=Name(lineno=347, col_offset=26, id='trans', ctx=Load()),
                            ),
                            keyword(
                                arg='unitdiag',
                                value=Name(lineno=347, col_offset=42, id='unit_diagonal', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=349,
                    col_offset=4,
                    test=Compare(
                        lineno=349,
                        col_offset=7,
                        left=Name(lineno=349, col_offset=7, id='info', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Num(lineno=349, col_offset=15, n=0)],
                    ),
                    body=[
                        Return(
                            lineno=350,
                            col_offset=8,
                            value=Name(lineno=350, col_offset=15, id='x', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=351,
                    col_offset=4,
                    test=Compare(
                        lineno=351,
                        col_offset=7,
                        left=Name(lineno=351, col_offset=7, id='info', ctx=Load()),
                        ops=[Gt()],
                        comparators=[Num(lineno=351, col_offset=14, n=0)],
                    ),
                    body=[
                        Raise(
                            lineno=352,
                            col_offset=8,
                            exc=Call(
                                lineno=352,
                                col_offset=14,
                                func=Name(lineno=352, col_offset=14, id='LinAlgError', ctx=Load()),
                                args=[
                                    BinOp(
                                        lineno=352,
                                        col_offset=26,
                                        left=Str(lineno=352, col_offset=26, s='singular matrix: resolution failed at diagonal %d'),
                                        op=Mod(),
                                        right=BinOp(
                                            lineno=353,
                                            col_offset=27,
                                            left=Name(lineno=353, col_offset=27, id='info', ctx=Load()),
                                            op=Sub(),
                                            right=Num(lineno=353, col_offset=32, n=1),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Raise(
                    lineno=354,
                    col_offset=4,
                    exc=Call(
                        lineno=354,
                        col_offset=10,
                        func=Name(lineno=354, col_offset=10, id='ValueError', ctx=Load()),
                        args=[
                            BinOp(
                                lineno=354,
                                col_offset=21,
                                left=Str(lineno=354, col_offset=21, s='illegal value in %d-th argument of internal trtrs'),
                                op=Mod(),
                                right=UnaryOp(
                                    lineno=355,
                                    col_offset=22,
                                    op=USub(),
                                    operand=Name(lineno=355, col_offset=23, id='info', ctx=Load()),
                                ),
                            ),
                        ],
                        keywords=[],
                    ),
                    cause=None,
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=358,
            col_offset=0,
            name='solve_banded',
            args=arguments(
                args=[
                    arg(lineno=358, col_offset=17, arg='l_and_u', annotation=None),
                    arg(lineno=358, col_offset=26, arg='ab', annotation=None),
                    arg(lineno=358, col_offset=30, arg='b', annotation=None),
                    arg(lineno=358, col_offset=33, arg='overwrite_ab', annotation=None),
                    arg(lineno=358, col_offset=53, arg='overwrite_b', annotation=None),
                    arg(lineno=359, col_offset=17, arg='debug', annotation=None),
                    arg(lineno=359, col_offset=29, arg='check_finite', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    NameConstant(lineno=358, col_offset=46, value=False),
                    NameConstant(lineno=358, col_offset=65, value=False),
                    NameConstant(lineno=359, col_offset=23, value=None),
                    NameConstant(lineno=359, col_offset=42, value=True),
                ],
            ),
            body=[
                Expr(
                    lineno=425,
                    col_offset=-1,
                    value=Str(lineno=425, col_offset=-1, s='\n    Solve the equation a x = b for x, assuming a is banded matrix.\n\n    The matrix a is stored in `ab` using the matrix diagonal ordered form::\n\n        ab[u + i - j, j] == a[i,j]\n\n    Example of `ab` (shape of a is (6,6), `u` =1, `l` =2)::\n\n        *    a01  a12  a23  a34  a45\n        a00  a11  a22  a33  a44  a55\n        a10  a21  a32  a43  a54   *\n        a20  a31  a42  a53   *    *\n\n    Parameters\n    ----------\n    (l, u) : (integer, integer)\n        Number of non-zero lower and upper diagonals\n    ab : (`l` + `u` + 1, M) array_like\n        Banded matrix\n    b : (M,) or (M, K) array_like\n        Right-hand side\n    overwrite_ab : bool, optional\n        Discard data in `ab` (may enhance performance)\n    overwrite_b : bool, optional\n        Discard data in `b` (may enhance performance)\n    check_finite : bool, optional\n        Whether to check that the input matrices contain only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n\n    Returns\n    -------\n    x : (M,) or (M, K) ndarray\n        The solution to the system a x = b.  Returned shape depends on the\n        shape of `b`.\n\n    Examples\n    --------\n    Solve the banded system a x = b, where::\n\n            [5  2 -1  0  0]       [0]\n            [1  4  2 -1  0]       [1]\n        a = [0  1  3  2 -1]   b = [2]\n            [0  0  1  2  2]       [2]\n            [0  0  0  1  1]       [3]\n\n    There is one nonzero diagonal below the main diagonal (l = 1), and\n    two above (u = 2).  The diagonal banded form of the matrix is::\n\n             [*  * -1 -1 -1]\n        ab = [*  2  2  2  2]\n             [5  4  3  2  1]\n             [1  1  1  1  *]\n\n    >>> from scipy.linalg import solve_banded\n    >>> ab = np.array([[0,  0, -1, -1, -1],\n    ...                [0,  2,  2,  2,  2],\n    ...                [5,  4,  3,  2,  1],\n    ...                [1,  1,  1,  1,  0]])\n    >>> b = np.array([0, 1, 2, 2, 3])\n    >>> x = solve_banded((1, 2), ab, b)\n    >>> x\n    array([-2.37288136,  3.93220339, -4.        ,  4.3559322 , -1.3559322 ])\n\n    '),
                ),
                If(
                    lineno=428,
                    col_offset=4,
                    test=Compare(
                        lineno=428,
                        col_offset=7,
                        left=Name(lineno=428, col_offset=7, id='debug', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[NameConstant(lineno=428, col_offset=20, value=None)],
                    ),
                    body=[
                        Expr(
                            lineno=429,
                            col_offset=8,
                            value=Call(
                                lineno=429,
                                col_offset=8,
                                func=Name(lineno=429, col_offset=8, id='warn', ctx=Load()),
                                args=[
                                    Str(lineno=429, col_offset=13, s='Use of the "debug" keyword is deprecated and this keyword will be removed in the future versions of SciPy.'),
                                    Name(lineno=431, col_offset=35, id='DeprecationWarning', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='stacklevel',
                                        value=Num(lineno=431, col_offset=66, n=2),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=433,
                    col_offset=4,
                    targets=[Name(lineno=433, col_offset=4, id='a1', ctx=Store())],
                    value=Call(
                        lineno=433,
                        col_offset=9,
                        func=Name(lineno=433, col_offset=9, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=433, col_offset=28, id='ab', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=433, col_offset=45, id='check_finite', ctx=Load()),
                            ),
                            keyword(
                                arg='as_inexact',
                                value=NameConstant(lineno=433, col_offset=70, value=True),
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=434,
                    col_offset=4,
                    targets=[Name(lineno=434, col_offset=4, id='b1', ctx=Store())],
                    value=Call(
                        lineno=434,
                        col_offset=9,
                        func=Name(lineno=434, col_offset=9, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=434, col_offset=28, id='b', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=434, col_offset=44, id='check_finite', ctx=Load()),
                            ),
                            keyword(
                                arg='as_inexact',
                                value=NameConstant(lineno=434, col_offset=69, value=True),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=436,
                    col_offset=4,
                    test=Compare(
                        lineno=436,
                        col_offset=7,
                        left=Subscript(
                            lineno=436,
                            col_offset=7,
                            value=Attribute(
                                lineno=436,
                                col_offset=7,
                                value=Name(lineno=436, col_offset=7, id='a1', ctx=Load()),
                                attr='shape',
                                ctx=Load(),
                            ),
                            slice=Index(
                                value=UnaryOp(
                                    lineno=436,
                                    col_offset=16,
                                    op=USub(),
                                    operand=Num(lineno=436, col_offset=17, n=1),
                                ),
                            ),
                            ctx=Load(),
                        ),
                        ops=[NotEq()],
                        comparators=[
                            Subscript(
                                lineno=436,
                                col_offset=23,
                                value=Attribute(
                                    lineno=436,
                                    col_offset=23,
                                    value=Name(lineno=436, col_offset=23, id='b1', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                                slice=Index(
                                    value=Num(lineno=436, col_offset=32, n=0),
                                ),
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            lineno=437,
                            col_offset=8,
                            exc=Call(
                                lineno=437,
                                col_offset=14,
                                func=Name(lineno=437, col_offset=14, id='ValueError', ctx=Load()),
                                args=[Str(lineno=437, col_offset=25, s='shapes of ab and b are not compatible.')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=438,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=438,
                            col_offset=5,
                            elts=[
                                Name(lineno=438, col_offset=5, id='nlower', ctx=Store()),
                                Name(lineno=438, col_offset=13, id='nupper', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Name(lineno=438, col_offset=23, id='l_and_u', ctx=Load()),
                ),
                If(
                    lineno=439,
                    col_offset=4,
                    test=Compare(
                        lineno=439,
                        col_offset=7,
                        left=BinOp(
                            lineno=439,
                            col_offset=23,
                            left=BinOp(
                                lineno=439,
                                col_offset=7,
                                left=Name(lineno=439, col_offset=7, id='nlower', ctx=Load()),
                                op=Add(),
                                right=Name(lineno=439, col_offset=16, id='nupper', ctx=Load()),
                            ),
                            op=Add(),
                            right=Num(lineno=439, col_offset=25, n=1),
                        ),
                        ops=[NotEq()],
                        comparators=[
                            Subscript(
                                lineno=439,
                                col_offset=30,
                                value=Attribute(
                                    lineno=439,
                                    col_offset=30,
                                    value=Name(lineno=439, col_offset=30, id='a1', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                                slice=Index(
                                    value=Num(lineno=439, col_offset=39, n=0),
                                ),
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            lineno=440,
                            col_offset=8,
                            exc=Call(
                                lineno=440,
                                col_offset=14,
                                func=Name(lineno=440, col_offset=14, id='ValueError', ctx=Load()),
                                args=[
                                    BinOp(
                                        lineno=440,
                                        col_offset=25,
                                        left=Str(lineno=440, col_offset=25, s='invalid values for the number of lower and upper diagonals: l+u+1 (%d) does not equal ab.shape[0] (%d)'),
                                        op=Mod(),
                                        right=Tuple(
                                            lineno=442,
                                            col_offset=35,
                                            elts=[
                                                BinOp(
                                                    lineno=442,
                                                    col_offset=51,
                                                    left=BinOp(
                                                        lineno=442,
                                                        col_offset=35,
                                                        left=Name(lineno=442, col_offset=35, id='nlower', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(lineno=442, col_offset=44, id='nupper', ctx=Load()),
                                                    ),
                                                    op=Add(),
                                                    right=Num(lineno=442, col_offset=53, n=1),
                                                ),
                                                Subscript(
                                                    lineno=442,
                                                    col_offset=56,
                                                    value=Attribute(
                                                        lineno=442,
                                                        col_offset=56,
                                                        value=Name(lineno=442, col_offset=56, id='ab', ctx=Load()),
                                                        attr='shape',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Index(
                                                        value=Num(lineno=442, col_offset=65, n=0),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=444,
                    col_offset=4,
                    targets=[Name(lineno=444, col_offset=4, id='overwrite_b', ctx=Store())],
                    value=BoolOp(
                        lineno=444,
                        col_offset=18,
                        op=Or(),
                        values=[
                            Name(lineno=444, col_offset=18, id='overwrite_b', ctx=Load()),
                            Call(
                                lineno=444,
                                col_offset=33,
                                func=Name(lineno=444, col_offset=33, id='_datacopied', ctx=Load()),
                                args=[
                                    Name(lineno=444, col_offset=45, id='b1', ctx=Load()),
                                    Name(lineno=444, col_offset=49, id='b', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=445,
                    col_offset=4,
                    test=Compare(
                        lineno=445,
                        col_offset=7,
                        left=Subscript(
                            lineno=445,
                            col_offset=7,
                            value=Attribute(
                                lineno=445,
                                col_offset=7,
                                value=Name(lineno=445, col_offset=7, id='a1', ctx=Load()),
                                attr='shape',
                                ctx=Load(),
                            ),
                            slice=Index(
                                value=UnaryOp(
                                    lineno=445,
                                    col_offset=16,
                                    op=USub(),
                                    operand=Num(lineno=445, col_offset=17, n=1),
                                ),
                            ),
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Num(lineno=445, col_offset=23, n=1)],
                    ),
                    body=[
                        Assign(
                            lineno=446,
                            col_offset=8,
                            targets=[Name(lineno=446, col_offset=8, id='b2', ctx=Store())],
                            value=Call(
                                lineno=446,
                                col_offset=13,
                                func=Attribute(
                                    lineno=446,
                                    col_offset=13,
                                    value=Name(lineno=446, col_offset=13, id='np', ctx=Load()),
                                    attr='array',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=446, col_offset=22, id='b1', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='copy',
                                        value=UnaryOp(
                                            lineno=446,
                                            col_offset=32,
                                            op=Not(),
                                            operand=Name(lineno=446, col_offset=36, id='overwrite_b', ctx=Load()),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        AugAssign(
                            lineno=447,
                            col_offset=8,
                            target=Name(lineno=447, col_offset=8, id='b2', ctx=Store()),
                            op=Div(),
                            value=Subscript(
                                lineno=447,
                                col_offset=14,
                                value=Name(lineno=447, col_offset=14, id='a1', ctx=Load()),
                                slice=Index(
                                    value=Tuple(
                                        lineno=447,
                                        col_offset=17,
                                        elts=[
                                            Num(lineno=447, col_offset=17, n=1),
                                            Num(lineno=447, col_offset=20, n=0),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                ctx=Load(),
                            ),
                        ),
                        Return(
                            lineno=448,
                            col_offset=8,
                            value=Name(lineno=448, col_offset=15, id='b2', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=449,
                    col_offset=4,
                    test=Compare(
                        lineno=449,
                        col_offset=7, left=Name(lineno=449, col_offset=7, id='nlower', ctx=Load()),
                        ops=[
                            Eq(),
                            Eq(),
                        ],
                        comparators=[
                            Name(lineno=449, col_offset=17, id='nupper', ctx=Load()),
                            Num(lineno=449, col_offset=27, n=1),
                        ],
                    ),
                    body=[
                        Assign(
                            lineno=450,
                            col_offset=8,
                            targets=[Name(lineno=450, col_offset=8, id='overwrite_ab', ctx=Store())],
                            value=BoolOp(
                                lineno=450,
                                col_offset=23,
                                op=Or(),
                                values=[
                                    Name(lineno=450, col_offset=23, id='overwrite_ab', ctx=Load()),
                                    Call(
                                        lineno=450,
                                        col_offset=39,
                                        func=Name(lineno=450, col_offset=39, id='_datacopied', ctx=Load()),
                                        args=[
                                            Name(lineno=450, col_offset=51, id='a1', ctx=Load()),
                                            Name(lineno=450, col_offset=55, id='ab', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            lineno=451,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=451,
                                    col_offset=8,
                                    elts=[Name(lineno=451, col_offset=8, id='gtsv', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=451,
                                col_offset=16,
                                func=Name(lineno=451, col_offset=16, id='get_lapack_funcs', ctx=Load()),
                                args=[
                                    Tuple(
                                        lineno=451,
                                        col_offset=34,
                                        elts=[Str(lineno=451, col_offset=34, s='gtsv')],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=451,
                                        col_offset=45,
                                        elts=[
                                            Name(lineno=451, col_offset=45, id='a1', ctx=Load()),
                                            Name(lineno=451, col_offset=49, id='b1', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=452,
                            col_offset=8,
                            targets=[Name(lineno=452, col_offset=8, id='du', ctx=Store())],
                            value=Subscript(
                                lineno=452,
                                col_offset=13,
                                value=Name(lineno=452, col_offset=13, id='a1', ctx=Load()),
                                slice=ExtSlice(
                                    dims=[
                                        Index(
                                            value=Num(lineno=452, col_offset=16, n=0),
                                        ),
                                        Slice(
                                            lower=Num(lineno=452, col_offset=19, n=1),
                                            upper=None,
                                            step=None,
                                        ),
                                    ],
                                ),
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            lineno=453,
                            col_offset=8,
                            targets=[Name(lineno=453, col_offset=8, id='d', ctx=Store())],
                            value=Subscript(
                                lineno=453,
                                col_offset=12,
                                value=Name(lineno=453, col_offset=12, id='a1', ctx=Load()),
                                slice=ExtSlice(
                                    dims=[
                                        Index(
                                            value=Num(lineno=453, col_offset=15, n=1),
                                        ),
                                        Slice(lower=None, upper=None, step=None),
                                    ],
                                ),
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            lineno=454,
                            col_offset=8,
                            targets=[Name(lineno=454, col_offset=8, id='dl', ctx=Store())],
                            value=Subscript(
                                lineno=454,
                                col_offset=13,
                                value=Name(lineno=454, col_offset=13, id='a1', ctx=Load()),
                                slice=ExtSlice(
                                    dims=[
                                        Index(
                                            value=Num(lineno=454, col_offset=16, n=2),
                                        ),
                                        Slice(
                                            lower=None,
                                            upper=UnaryOp(
                                                lineno=454,
                                                col_offset=20,
                                                op=USub(),
                                                operand=Num(lineno=454, col_offset=21, n=1),
                                            ),
                                            step=None,
                                        ),
                                    ],
                                ),
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            lineno=455,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=455,
                                    col_offset=8,
                                    elts=[
                                        Name(lineno=455, col_offset=8, id='du2', ctx=Store()),
                                        Name(lineno=455, col_offset=13, id='d', ctx=Store()),
                                        Name(lineno=455, col_offset=16, id='du', ctx=Store()),
                                        Name(lineno=455, col_offset=20, id='x', ctx=Store()),
                                        Name(lineno=455, col_offset=23, id='info', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=455,
                                col_offset=30,
                                func=Name(lineno=455, col_offset=30, id='gtsv', ctx=Load()),
                                args=[
                                    Name(lineno=455, col_offset=35, id='dl', ctx=Load()),
                                    Name(lineno=455, col_offset=39, id='d', ctx=Load()),
                                    Name(lineno=455, col_offset=42, id='du', ctx=Load()),
                                    Name(lineno=455, col_offset=46, id='b1', ctx=Load()),
                                    Name(lineno=455, col_offset=50, id='overwrite_ab', ctx=Load()),
                                    Name(lineno=455, col_offset=64, id='overwrite_ab', ctx=Load()),
                                    Name(lineno=456, col_offset=35, id='overwrite_ab', ctx=Load()),
                                    Name(lineno=456, col_offset=49, id='overwrite_b', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[
                        Assign(
                            lineno=458,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=458,
                                    col_offset=8,
                                    elts=[Name(lineno=458, col_offset=8, id='gbsv', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=458,
                                col_offset=16,
                                func=Name(lineno=458, col_offset=16, id='get_lapack_funcs', ctx=Load()),
                                args=[
                                    Tuple(
                                        lineno=458,
                                        col_offset=34,
                                        elts=[Str(lineno=458, col_offset=34, s='gbsv')],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=458,
                                        col_offset=45,
                                        elts=[
                                            Name(lineno=458, col_offset=45, id='a1', ctx=Load()),
                                            Name(lineno=458, col_offset=49, id='b1', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=459,
                            col_offset=8,
                            targets=[Name(lineno=459, col_offset=8, id='a2', ctx=Store())],
                            value=Call(
                                lineno=459,
                                col_offset=13,
                                func=Attribute(
                                    lineno=459,
                                    col_offset=13,
                                    value=Name(lineno=459, col_offset=13, id='np', ctx=Load()),
                                    attr='zeros',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        lineno=459,
                                        col_offset=23,
                                        elts=[
                                            BinOp(
                                                lineno=459,
                                                col_offset=41,
                                                left=BinOp(
                                                    lineno=459,
                                                    col_offset=23,
                                                    left=BinOp(
                                                        lineno=459,
                                                        col_offset=23,
                                                        left=Num(lineno=459, col_offset=23, n=2),
                                                        op=Mult(),
                                                        right=Name(lineno=459, col_offset=25, id='nlower', ctx=Load()),
                                                    ),
                                                    op=Add(),
                                                    right=Name(lineno=459, col_offset=34, id='nupper', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Num(lineno=459, col_offset=43, n=1),
                                            ),
                                            Subscript(
                                                lineno=459,
                                                col_offset=46,
                                                value=Attribute(
                                                    lineno=459,
                                                    col_offset=46,
                                                    value=Name(lineno=459, col_offset=46, id='a1', ctx=Load()),
                                                    attr='shape',
                                                    ctx=Load(),
                                                ),
                                                slice=Index(
                                                    value=Num(lineno=459, col_offset=55, n=1),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dtype',
                                        value=Attribute(
                                            lineno=459,
                                            col_offset=66,
                                            value=Name(lineno=459, col_offset=66, id='gbsv', ctx=Load()),
                                            attr='dtype',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            lineno=460,
                            col_offset=8,
                            targets=[
                                Subscript(
                                    lineno=460,
                                    col_offset=8,
                                    value=Name(lineno=460, col_offset=8, id='a2', ctx=Load()),
                                    slice=ExtSlice(
                                        dims=[
                                            Slice(
                                                lower=Name(lineno=460, col_offset=11, id='nlower', ctx=Load()),
                                                upper=None,
                                                step=None,
                                            ),
                                            Slice(lower=None, upper=None, step=None),
                                        ],
                                    ),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(lineno=460, col_offset=25, id='a1', ctx=Load()),
                        ),
                        Assign(
                            lineno=461,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=461,
                                    col_offset=8,
                                    elts=[
                                        Name(lineno=461, col_offset=8, id='lu', ctx=Store()),
                                        Name(lineno=461, col_offset=12, id='piv', ctx=Store()),
                                        Name(lineno=461, col_offset=17, id='x', ctx=Store()),
                                        Name(lineno=461, col_offset=20, id='info', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=461,
                                col_offset=27,
                                func=Name(lineno=461, col_offset=27, id='gbsv', ctx=Load()),
                                args=[
                                    Name(lineno=461, col_offset=32, id='nlower', ctx=Load()),
                                    Name(lineno=461, col_offset=40, id='nupper', ctx=Load()),
                                    Name(lineno=461, col_offset=48, id='a2', ctx=Load()),
                                    Name(lineno=461, col_offset=52, id='b1', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='overwrite_ab',
                                        value=NameConstant(lineno=461, col_offset=69, value=True),
                                    ),
                                    keyword(
                                        arg='overwrite_b',
                                        value=Name(lineno=462, col_offset=44, id='overwrite_b', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                If(
                    lineno=463,
                    col_offset=4,
                    test=Compare(
                        lineno=463,
                        col_offset=7,
                        left=Name(lineno=463, col_offset=7, id='info', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Num(lineno=463, col_offset=15, n=0)],
                    ),
                    body=[
                        Return(
                            lineno=464,
                            col_offset=8,
                            value=Name(lineno=464, col_offset=15, id='x', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=465,
                    col_offset=4,
                    test=Compare(
                        lineno=465,
                        col_offset=7,
                        left=Name(lineno=465, col_offset=7, id='info', ctx=Load()),
                        ops=[Gt()],
                        comparators=[Num(lineno=465, col_offset=14, n=0)],
                    ),
                    body=[
                        Raise(
                            lineno=466,
                            col_offset=8,
                            exc=Call(
                                lineno=466,
                                col_offset=14,
                                func=Name(lineno=466, col_offset=14, id='LinAlgError', ctx=Load()),
                                args=[Str(lineno=466, col_offset=26, s='singular matrix')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Raise(
                    lineno=467,
                    col_offset=4,
                    exc=Call(
                        lineno=467,
                        col_offset=10,
                        func=Name(lineno=467, col_offset=10, id='ValueError', ctx=Load()),
                        args=[
                            BinOp(
                                lineno=467,
                                col_offset=21,
                                left=Str(lineno=467, col_offset=21, s='illegal value in %d-th argument of internal gbsv/gtsv'),
                                op=Mod(),
                                right=UnaryOp(
                                    lineno=468,
                                    col_offset=35,
                                    op=USub(),
                                    operand=Name(lineno=468, col_offset=36, id='info', ctx=Load()),
                                ),
                            ),
                        ],
                        keywords=[],
                    ),
                    cause=None,
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=471,
            col_offset=0,
            name='solveh_banded',
            args=arguments(
                args=[
                    arg(lineno=471, col_offset=18, arg='ab', annotation=None),
                    arg(lineno=471, col_offset=22, arg='b', annotation=None),
                    arg(lineno=471, col_offset=25, arg='overwrite_ab', annotation=None),
                    arg(lineno=471, col_offset=45, arg='overwrite_b', annotation=None),
                    arg(lineno=471, col_offset=64, arg='lower', annotation=None),
                    arg(lineno=472, col_offset=18, arg='check_finite', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    NameConstant(lineno=471, col_offset=38, value=False),
                    NameConstant(lineno=471, col_offset=57, value=False),
                    NameConstant(lineno=471, col_offset=70, value=False),
                    NameConstant(lineno=472, col_offset=31, value=True),
                ],
            ),
            body=[
                Expr(
                    lineno=562,
                    col_offset=-1,
                    value=Str(lineno=562, col_offset=-1, s='\n    Solve equation a x = b. a is Hermitian positive-definite banded matrix.\n\n    The matrix a is stored in `ab` either in lower diagonal or upper\n    diagonal ordered form:\n\n        ab[u + i - j, j] == a[i,j]        (if upper form; i <= j)\n        ab[    i - j, j] == a[i,j]        (if lower form; i >= j)\n\n    Example of `ab` (shape of a is (6, 6), `u` =2)::\n\n        upper form:\n        *   *   a02 a13 a24 a35\n        *   a01 a12 a23 a34 a45\n        a00 a11 a22 a33 a44 a55\n\n        lower form:\n        a00 a11 a22 a33 a44 a55\n        a10 a21 a32 a43 a54 *\n        a20 a31 a42 a53 *   *\n\n    Cells marked with * are not used.\n\n    Parameters\n    ----------\n    ab : (`u` + 1, M) array_like\n        Banded matrix\n    b : (M,) or (M, K) array_like\n        Right-hand side\n    overwrite_ab : bool, optional\n        Discard data in `ab` (may enhance performance)\n    overwrite_b : bool, optional\n        Discard data in `b` (may enhance performance)\n    lower : bool, optional\n        Is the matrix in the lower form. (Default is upper form)\n    check_finite : bool, optional\n        Whether to check that the input matrices contain only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n\n    Returns\n    -------\n    x : (M,) or (M, K) ndarray\n        The solution to the system a x = b.  Shape of return matches shape\n        of `b`.\n\n    Examples\n    --------\n    Solve the banded system A x = b, where::\n\n            [ 4  2 -1  0  0  0]       [1]\n            [ 2  5  2 -1  0  0]       [2]\n        A = [-1  2  6  2 -1  0]   b = [2]\n            [ 0 -1  2  7  2 -1]       [3]\n            [ 0  0 -1  2  8  2]       [3]\n            [ 0  0  0 -1  2  9]       [3]\n\n    >>> from scipy.linalg import solveh_banded\n\n    `ab` contains the main diagonal and the nonzero diagonals below the\n    main diagonal.  That is, we use the lower form:\n\n    >>> ab = np.array([[ 4,  5,  6,  7, 8, 9],\n    ...                [ 2,  2,  2,  2, 2, 0],\n    ...                [-1, -1, -1, -1, 0, 0]])\n    >>> b = np.array([1, 2, 2, 3, 3, 3])\n    >>> x = solveh_banded(ab, b, lower=True)\n    >>> x\n    array([ 0.03431373,  0.45938375,  0.05602241,  0.47759104,  0.17577031,\n            0.34733894])\n\n\n    Solve the Hermitian banded system H x = b, where::\n\n            [ 8   2-1j   0     0  ]        [ 1  ]\n        H = [2+1j  5     1j    0  ]    b = [1+1j]\n            [ 0   -1j    9   -2-1j]        [1-2j]\n            [ 0    0   -2+1j   6  ]        [ 0  ]\n\n    In this example, we put the upper diagonals in the array `hb`:\n\n    >>> hb = np.array([[0, 2-1j, 1j, -2-1j],\n    ...                [8,  5,    9,   6  ]])\n    >>> b = np.array([1, 1+1j, 1-2j, 0])\n    >>> x = solveh_banded(hb, b)\n    >>> x\n    array([ 0.07318536-0.02939412j,  0.11877624+0.17696461j,\n            0.10077984-0.23035393j, -0.00479904-0.09358128j])\n\n    '),
                ),
                Assign(
                    lineno=563,
                    col_offset=4,
                    targets=[Name(lineno=563, col_offset=4, id='a1', ctx=Store())],
                    value=Call(
                        lineno=563,
                        col_offset=9,
                        func=Name(lineno=563, col_offset=9, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=563, col_offset=28, id='ab', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=563, col_offset=45, id='check_finite', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=564,
                    col_offset=4,
                    targets=[Name(lineno=564, col_offset=4, id='b1', ctx=Store())],
                    value=Call(
                        lineno=564,
                        col_offset=9,
                        func=Name(lineno=564, col_offset=9, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=564, col_offset=28, id='b', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=564, col_offset=44, id='check_finite', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=566,
                    col_offset=4,
                    test=Compare(
                        lineno=566,
                        col_offset=7,
                        left=Subscript(
                            lineno=566,
                            col_offset=7,
                            value=Attribute(
                                lineno=566,
                                col_offset=7,
                                value=Name(lineno=566, col_offset=7, id='a1', ctx=Load()),
                                attr='shape',
                                ctx=Load(),
                            ),
                            slice=Index(
                                value=UnaryOp(
                                    lineno=566,
                                    col_offset=16,
                                    op=USub(),
                                    operand=Num(lineno=566, col_offset=17, n=1),
                                ),
                            ),
                            ctx=Load(),
                        ),
                        ops=[NotEq()],
                        comparators=[
                            Subscript(
                                lineno=566,
                                col_offset=23,
                                value=Attribute(
                                    lineno=566,
                                    col_offset=23,
                                    value=Name(lineno=566, col_offset=23, id='b1', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                                slice=Index(
                                    value=Num(lineno=566, col_offset=32, n=0),
                                ),
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            lineno=567,
                            col_offset=8,
                            exc=Call(
                                lineno=567,
                                col_offset=14,
                                func=Name(lineno=567, col_offset=14, id='ValueError', ctx=Load()),
                                args=[Str(lineno=567, col_offset=25, s='shapes of ab and b are not compatible.')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=569,
                    col_offset=4,
                    targets=[Name(lineno=569, col_offset=4, id='overwrite_b', ctx=Store())],
                    value=BoolOp(
                        lineno=569,
                        col_offset=18,
                        op=Or(),
                        values=[
                            Name(lineno=569, col_offset=18, id='overwrite_b', ctx=Load()),
                            Call(
                                lineno=569,
                                col_offset=33,
                                func=Name(lineno=569, col_offset=33, id='_datacopied', ctx=Load()),
                                args=[
                                    Name(lineno=569, col_offset=45, id='b1', ctx=Load()),
                                    Name(lineno=569, col_offset=49, id='b', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=570,
                    col_offset=4,
                    targets=[Name(lineno=570, col_offset=4, id='overwrite_ab', ctx=Store())],
                    value=BoolOp(
                        lineno=570,
                        col_offset=19,
                        op=Or(),
                        values=[
                            Name(lineno=570, col_offset=19, id='overwrite_ab', ctx=Load()),
                            Call(
                                lineno=570,
                                col_offset=35,
                                func=Name(lineno=570, col_offset=35, id='_datacopied', ctx=Load()),
                                args=[
                                    Name(lineno=570, col_offset=47, id='a1', ctx=Load()),
                                    Name(lineno=570, col_offset=51, id='ab', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=572,
                    col_offset=4,
                    test=Compare(
                        lineno=572,
                        col_offset=7,
                        left=Subscript(
                            lineno=572,
                            col_offset=7,
                            value=Attribute(
                                lineno=572,
                                col_offset=7,
                                value=Name(lineno=572, col_offset=7, id='a1', ctx=Load()),
                                attr='shape',
                                ctx=Load(),
                            ),
                            slice=Index(
                                value=Num(lineno=572, col_offset=16, n=0),
                            ),
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Num(lineno=572, col_offset=22, n=2)],
                    ),
                    body=[
                        Assign(
                            lineno=573,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=573,
                                    col_offset=8,
                                    elts=[Name(lineno=573, col_offset=8, id='ptsv', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=573,
                                col_offset=16,
                                func=Name(lineno=573, col_offset=16, id='get_lapack_funcs', ctx=Load()),
                                args=[
                                    Tuple(
                                        lineno=573,
                                        col_offset=34,
                                        elts=[Str(lineno=573, col_offset=34, s='ptsv')],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=573,
                                        col_offset=45,
                                        elts=[
                                            Name(lineno=573, col_offset=45, id='a1', ctx=Load()),
                                            Name(lineno=573, col_offset=49, id='b1', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            lineno=574,
                            col_offset=8,
                            test=Name(lineno=574, col_offset=11, id='lower', ctx=Load()),
                            body=[
                                Assign(
                                    lineno=575,
                                    col_offset=12,
                                    targets=[Name(lineno=575, col_offset=12, id='d', ctx=Store())],
                                    value=Attribute(
                                        lineno=575,
                                        col_offset=16,
                                        value=Subscript(
                                            lineno=575,
                                            col_offset=16,
                                            value=Name(lineno=575, col_offset=16, id='a1', ctx=Load()),
                                            slice=ExtSlice(
                                                dims=[
                                                    Index(
                                                        value=Num(lineno=575, col_offset=19, n=0),
                                                    ),
                                                    Slice(lower=None, upper=None, step=None),
                                                ],
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='real',
                                        ctx=Load(),
                                    ),
                                ),
                                Assign(
                                    lineno=576,
                                    col_offset=12,
                                    targets=[Name(lineno=576, col_offset=12, id='e', ctx=Store())],
                                    value=Subscript(
                                        lineno=576,
                                        col_offset=16,
                                        value=Name(lineno=576, col_offset=16, id='a1', ctx=Load()),
                                        slice=ExtSlice(
                                            dims=[
                                                Index(
                                                    value=Num(lineno=576, col_offset=19, n=1),
                                                ),
                                                Slice(
                                                    lower=None,
                                                    upper=UnaryOp(
                                                        lineno=576,
                                                        col_offset=23,
                                                        op=USub(),
                                                        operand=Num(lineno=576, col_offset=24, n=1),
                                                    ),
                                                    step=None,
                                                ),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    lineno=578,
                                    col_offset=12,
                                    targets=[Name(lineno=578, col_offset=12, id='d', ctx=Store())],
                                    value=Attribute(
                                        lineno=578,
                                        col_offset=16,
                                        value=Subscript(
                                            lineno=578,
                                            col_offset=16,
                                            value=Name(lineno=578, col_offset=16, id='a1', ctx=Load()),
                                            slice=ExtSlice(
                                                dims=[
                                                    Index(
                                                        value=Num(lineno=578, col_offset=19, n=1),
                                                    ),
                                                    Slice(lower=None, upper=None, step=None),
                                                ],
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='real',
                                        ctx=Load(),
                                    ),
                                ),
                                Assign(
                                    lineno=579,
                                    col_offset=12,
                                    targets=[Name(lineno=579, col_offset=12, id='e', ctx=Store())],
                                    value=Call(
                                        lineno=579,
                                        col_offset=16,
                                        func=Attribute(
                                            lineno=579,
                                            col_offset=16,
                                            value=Subscript(
                                                lineno=579,
                                                col_offset=16,
                                                value=Name(lineno=579, col_offset=16, id='a1', ctx=Load()),
                                                slice=ExtSlice(
                                                    dims=[
                                                        Index(
                                                            value=Num(lineno=579, col_offset=19, n=0),
                                                        ),
                                                        Slice(
                                                            lower=Num(lineno=579, col_offset=22, n=1),
                                                            upper=None,
                                                            step=None,
                                                        ),
                                                    ],
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='conj',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Assign(
                            lineno=580,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=580,
                                    col_offset=8,
                                    elts=[
                                        Name(lineno=580, col_offset=8, id='d', ctx=Store()),
                                        Name(lineno=580, col_offset=11, id='du', ctx=Store()),
                                        Name(lineno=580, col_offset=15, id='x', ctx=Store()),
                                        Name(lineno=580, col_offset=18, id='info', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=580,
                                col_offset=25,
                                func=Name(lineno=580, col_offset=25, id='ptsv', ctx=Load()),
                                args=[
                                    Name(lineno=580, col_offset=30, id='d', ctx=Load()),
                                    Name(lineno=580, col_offset=33, id='e', ctx=Load()),
                                    Name(lineno=580, col_offset=36, id='b1', ctx=Load()),
                                    Name(lineno=580, col_offset=40, id='overwrite_ab', ctx=Load()),
                                    Name(lineno=580, col_offset=54, id='overwrite_ab', ctx=Load()),
                                    Name(lineno=581, col_offset=30, id='overwrite_b', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[
                        Assign(
                            lineno=583,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=583,
                                    col_offset=8,
                                    elts=[Name(lineno=583, col_offset=8, id='pbsv', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=583,
                                col_offset=16,
                                func=Name(lineno=583, col_offset=16, id='get_lapack_funcs', ctx=Load()),
                                args=[
                                    Tuple(
                                        lineno=583,
                                        col_offset=34,
                                        elts=[Str(lineno=583, col_offset=34, s='pbsv')],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        lineno=583,
                                        col_offset=45,
                                        elts=[
                                            Name(lineno=583, col_offset=45, id='a1', ctx=Load()),
                                            Name(lineno=583, col_offset=49, id='b1', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=584,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=584,
                                    col_offset=8,
                                    elts=[
                                        Name(lineno=584, col_offset=8, id='c', ctx=Store()),
                                        Name(lineno=584, col_offset=11, id='x', ctx=Store()),
                                        Name(lineno=584, col_offset=14, id='info', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=584,
                                col_offset=21,
                                func=Name(lineno=584, col_offset=21, id='pbsv', ctx=Load()),
                                args=[
                                    Name(lineno=584, col_offset=26, id='a1', ctx=Load()),
                                    Name(lineno=584, col_offset=30, id='b1', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='lower',
                                        value=Name(lineno=584, col_offset=40, id='lower', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='overwrite_ab',
                                        value=Name(lineno=584, col_offset=60, id='overwrite_ab', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='overwrite_b',
                                        value=Name(lineno=585, col_offset=38, id='overwrite_b', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                If(
                    lineno=586,
                    col_offset=4,
                    test=Compare(
                        lineno=586,
                        col_offset=7,
                        left=Name(lineno=586, col_offset=7, id='info', ctx=Load()),
                        ops=[Gt()],
                        comparators=[Num(lineno=586, col_offset=14, n=0)],
                    ),
                    body=[
                        Raise(
                            lineno=587,
                            col_offset=8,
                            exc=Call(
                                lineno=587,
                                col_offset=14,
                                func=Name(lineno=587, col_offset=14, id='LinAlgError', ctx=Load()),
                                args=[
                                    BinOp(
                                        lineno=587,
                                        col_offset=26,
                                        left=Str(lineno=587, col_offset=26, s='%d-th leading minor not positive definite'),
                                        op=Mod(),
                                        right=Name(lineno=587, col_offset=72, id='info', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=588,
                    col_offset=4,
                    test=Compare(
                        lineno=588,
                        col_offset=7,
                        left=Name(lineno=588, col_offset=7, id='info', ctx=Load()),
                        ops=[Lt()],
                        comparators=[Num(lineno=588, col_offset=14, n=0)],
                    ),
                    body=[
                        Raise(
                            lineno=589,
                            col_offset=8,
                            exc=Call(
                                lineno=589,
                                col_offset=14,
                                func=Name(lineno=589, col_offset=14, id='ValueError', ctx=Load()),
                                args=[
                                    BinOp(
                                        lineno=589,
                                        col_offset=25,
                                        left=Str(lineno=589, col_offset=25, s='illegal value in %d-th argument of internal pbsv'),
                                        op=Mod(),
                                        right=UnaryOp(
                                            lineno=590,
                                            col_offset=34,
                                            op=USub(),
                                            operand=Name(lineno=590, col_offset=35, id='info', ctx=Load()),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    lineno=591,
                    col_offset=4,
                    value=Name(lineno=591, col_offset=11, id='x', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=594,
            col_offset=0,
            name='solve_toeplitz',
            args=arguments(
                args=[
                    arg(lineno=594, col_offset=19, arg='c_or_cr', annotation=None),
                    arg(lineno=594, col_offset=28, arg='b', annotation=None),
                    arg(lineno=594, col_offset=31, arg='check_finite', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[NameConstant(lineno=594, col_offset=44, value=True)],
            ),
            body=[
                Expr(
                    lineno=660,
                    col_offset=-1,
                    value=Str(lineno=660, col_offset=-1, s='Solve a Toeplitz system using Levinson Recursion\n\n    The Toeplitz matrix has constant diagonals, with c as its first column\n    and r as its first row.  If r is not given, ``r == conjugate(c)`` is\n    assumed.\n\n    Parameters\n    ----------\n    c_or_cr : array_like or tuple of (array_like, array_like)\n        The vector ``c``, or a tuple of arrays (``c``, ``r``). Whatever the\n        actual shape of ``c``, it will be converted to a 1-D array. If not\n        supplied, ``r = conjugate(c)`` is assumed; in this case, if c[0] is\n        real, the Toeplitz matrix is Hermitian. r[0] is ignored; the first row\n        of the Toeplitz matrix is ``[c[0], r[1:]]``.  Whatever the actual shape\n        of ``r``, it will be converted to a 1-D array.\n    b : (M,) or (M, K) array_like\n        Right-hand side in ``T x = b``.\n    check_finite : bool, optional\n        Whether to check that the input matrices contain only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (result entirely NaNs) if the inputs do contain infinities or NaNs.\n\n    Returns\n    -------\n    x : (M,) or (M, K) ndarray\n        The solution to the system ``T x = b``.  Shape of return matches shape\n        of `b`.\n\n    See Also\n    --------\n    toeplitz : Toeplitz matrix\n\n    Notes\n    -----\n    The solution is computed using Levinson-Durbin recursion, which is faster\n    than generic least-squares methods, but can be less numerically stable.\n\n    Examples\n    --------\n    Solve the Toeplitz system T x = b, where::\n\n            [ 1 -1 -2 -3]       [1]\n        T = [ 3  1 -1 -2]   b = [2]\n            [ 6  3  1 -1]       [2]\n            [10  6  3  1]       [5]\n\n    To specify the Toeplitz matrix, only the first column and the first\n    row are needed.\n\n    >>> c = np.array([1, 3, 6, 10])    # First column of T\n    >>> r = np.array([1, -1, -2, -3])  # First row of T\n    >>> b = np.array([1, 2, 2, 5])\n\n    >>> from scipy.linalg import solve_toeplitz, toeplitz\n    >>> x = solve_toeplitz((c, r), b)\n    >>> x\n    array([ 1.66666667, -1.        , -2.66666667,  2.33333333])\n\n    Check the result by creating the full Toeplitz matrix and\n    multiplying it by `x`.  We should get `b`.\n\n    >>> T = toeplitz(c, r)\n    >>> T.dot(x)\n    array([ 1.,  2.,  2.,  5.])\n\n    '),
                ),
                If(
                    lineno=664,
                    col_offset=4,
                    test=Call(
                        lineno=664,
                        col_offset=7,
                        func=Name(lineno=664, col_offset=7, id='isinstance', ctx=Load()),
                        args=[
                            Name(lineno=664, col_offset=18, id='c_or_cr', ctx=Load()),
                            Name(lineno=664, col_offset=27, id='tuple', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            lineno=665,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=665,
                                    col_offset=8,
                                    elts=[
                                        Name(lineno=665, col_offset=8, id='c', ctx=Store()),
                                        Name(lineno=665, col_offset=11, id='r', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(lineno=665, col_offset=15, id='c_or_cr', ctx=Load()),
                        ),
                        Assign(
                            lineno=666,
                            col_offset=8,
                            targets=[Name(lineno=666, col_offset=8, id='c', ctx=Store())],
                            value=Call(
                                lineno=666,
                                col_offset=12,
                                func=Attribute(
                                    lineno=666,
                                    col_offset=12,
                                    value=Call(
                                        lineno=666,
                                        col_offset=12,
                                        func=Name(lineno=666, col_offset=12, id='_asarray_validated', ctx=Load()),
                                        args=[Name(lineno=666, col_offset=31, id='c', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='check_finite',
                                                value=Name(lineno=666, col_offset=47, id='check_finite', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='ravel',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=667,
                            col_offset=8,
                            targets=[Name(lineno=667, col_offset=8, id='r', ctx=Store())],
                            value=Call(
                                lineno=667,
                                col_offset=12,
                                func=Attribute(
                                    lineno=667,
                                    col_offset=12,
                                    value=Call(
                                        lineno=667,
                                        col_offset=12,
                                        func=Name(lineno=667, col_offset=12, id='_asarray_validated', ctx=Load()),
                                        args=[Name(lineno=667, col_offset=31, id='r', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='check_finite',
                                                value=Name(lineno=667, col_offset=47, id='check_finite', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='ravel',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[
                        Assign(
                            lineno=669,
                            col_offset=8,
                            targets=[Name(lineno=669, col_offset=8, id='c', ctx=Store())],
                            value=Call(
                                lineno=669,
                                col_offset=12,
                                func=Attribute(
                                    lineno=669,
                                    col_offset=12,
                                    value=Call(
                                        lineno=669,
                                        col_offset=12,
                                        func=Name(lineno=669, col_offset=12, id='_asarray_validated', ctx=Load()),
                                        args=[Name(lineno=669, col_offset=31, id='c_or_cr', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='check_finite',
                                                value=Name(lineno=669, col_offset=53, id='check_finite', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='ravel',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=670,
                            col_offset=8,
                            targets=[Name(lineno=670, col_offset=8, id='r', ctx=Store())],
                            value=Call(
                                lineno=670,
                                col_offset=12,
                                func=Attribute(
                                    lineno=670,
                                    col_offset=12,
                                    value=Name(lineno=670, col_offset=12, id='c', ctx=Load()),
                                    attr='conjugate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                ),
                Assign(
                    lineno=674,
                    col_offset=4,
                    targets=[Name(lineno=674, col_offset=4, id='vals', ctx=Store())],
                    value=Call(
                        lineno=674,
                        col_offset=11,
                        func=Attribute(
                            lineno=674,
                            col_offset=11,
                            value=Name(lineno=674, col_offset=11, id='np', ctx=Load()),
                            attr='concatenate',
                            ctx=Load(),
                        ),
                        args=[
                            Tuple(
                                lineno=674,
                                col_offset=27,
                                elts=[
                                    Subscript(
                                        lineno=674,
                                        col_offset=27,
                                        value=Name(lineno=674, col_offset=27, id='r', ctx=Load()),
                                        slice=Slice(
                                            lower=UnaryOp(
                                                lineno=674,
                                                col_offset=29,
                                                op=USub(),
                                                operand=Num(lineno=674, col_offset=30, n=1),
                                            ),
                                            upper=Num(lineno=674, col_offset=32, n=0),
                                            step=UnaryOp(
                                                lineno=674,
                                                col_offset=34,
                                                op=USub(),
                                                operand=Num(lineno=674, col_offset=35, n=1),
                                            ),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Name(lineno=674, col_offset=39, id='c', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=675,
                    col_offset=4,
                    test=Compare(
                        lineno=675,
                        col_offset=7,
                        left=Name(lineno=675, col_offset=7, id='b', ctx=Load()),
                        ops=[Is()],
                        comparators=[NameConstant(lineno=675, col_offset=12, value=None)],
                    ),
                    body=[
                        Raise(
                            lineno=676,
                            col_offset=8,
                            exc=Call(
                                lineno=676,
                                col_offset=14,
                                func=Name(lineno=676, col_offset=14, id='ValueError', ctx=Load()),
                                args=[Str(lineno=676, col_offset=25, s='illegal value, `b` is a required argument')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=678,
                    col_offset=4,
                    targets=[Name(lineno=678, col_offset=4, id='b', ctx=Store())],
                    value=Call(
                        lineno=678,
                        col_offset=8,
                        func=Name(lineno=678, col_offset=8, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=678, col_offset=27, id='b', ctx=Load())],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=679,
                    col_offset=4,
                    test=Compare(
                        lineno=679,
                        col_offset=7,
                        left=Subscript(
                            lineno=679,
                            col_offset=7,
                            value=Attribute(
                                lineno=679,
                                col_offset=7,
                                value=Name(lineno=679, col_offset=7, id='vals', ctx=Load()),
                                attr='shape',
                                ctx=Load(),
                            ),
                            slice=Index(
                                value=Num(lineno=679, col_offset=18, n=0),
                            ),
                            ctx=Load(),
                        ),
                        ops=[NotEq()],
                        comparators=[
                            BinOp(
                                lineno=679,
                                col_offset=25,
                                left=BinOp(
                                    lineno=679,
                                    col_offset=25,
                                    left=Num(lineno=679, col_offset=25, n=2),
                                    op=Mult(),
                                    right=Subscript(
                                        lineno=679,
                                        col_offset=27,
                                        value=Attribute(
                                            lineno=679,
                                            col_offset=27,
                                            value=Name(lineno=679, col_offset=27, id='b', ctx=Load()),
                                            attr='shape',
                                            ctx=Load(),
                                        ),
                                        slice=Index(
                                            value=Num(lineno=679, col_offset=35, n=0),
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                                op=Sub(),
                                right=Num(lineno=679, col_offset=40, n=1),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            lineno=680,
                            col_offset=8,
                            exc=Call(
                                lineno=680,
                                col_offset=14,
                                func=Name(lineno=680, col_offset=14, id='ValueError', ctx=Load()),
                                args=[Str(lineno=680, col_offset=25, s='incompatible dimensions')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=681,
                    col_offset=4,
                    test=BoolOp(
                        lineno=681,
                        col_offset=7,
                        op=Or(),
                        values=[
                            Call(
                                lineno=681,
                                col_offset=7,
                                func=Attribute(
                                    lineno=681,
                                    col_offset=7,
                                    value=Name(lineno=681, col_offset=7, id='np', ctx=Load()),
                                    attr='iscomplexobj',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=681, col_offset=23, id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            Call(
                                lineno=681,
                                col_offset=32,
                                func=Attribute(
                                    lineno=681,
                                    col_offset=32,
                                    value=Name(lineno=681, col_offset=32, id='np', ctx=Load()),
                                    attr='iscomplexobj',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=681, col_offset=48, id='b', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            lineno=682,
                            col_offset=8,
                            targets=[Name(lineno=682, col_offset=8, id='vals', ctx=Store())],
                            value=Call(
                                lineno=682,
                                col_offset=15,
                                func=Attribute(
                                    lineno=682,
                                    col_offset=15,
                                    value=Name(lineno=682, col_offset=15, id='np', ctx=Load()),
                                    attr='asarray',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=682, col_offset=26, id='vals', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='dtype',
                                        value=Attribute(
                                            lineno=682,
                                            col_offset=38,
                                            value=Name(lineno=682, col_offset=38, id='np', ctx=Load()),
                                            attr='complex128',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='order',
                                        value=Str(lineno=682, col_offset=59, s='c'),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            lineno=683,
                            col_offset=8,
                            targets=[Name(lineno=683, col_offset=8, id='b', ctx=Store())],
                            value=Call(
                                lineno=683,
                                col_offset=12,
                                func=Attribute(
                                    lineno=683,
                                    col_offset=12,
                                    value=Name(lineno=683, col_offset=12, id='np', ctx=Load()),
                                    attr='asarray',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=683, col_offset=23, id='b', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='dtype',
                                        value=Attribute(
                                            lineno=683,
                                            col_offset=32,
                                            value=Name(lineno=683, col_offset=32, id='np', ctx=Load()),
                                            attr='complex128',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[
                        Assign(
                            lineno=685,
                            col_offset=8,
                            targets=[Name(lineno=685, col_offset=8, id='vals', ctx=Store())],
                            value=Call(
                                lineno=685,
                                col_offset=15,
                                func=Attribute(
                                    lineno=685,
                                    col_offset=15,
                                    value=Name(lineno=685, col_offset=15, id='np', ctx=Load()),
                                    attr='asarray',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=685, col_offset=26, id='vals', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='dtype',
                                        value=Attribute(
                                            lineno=685,
                                            col_offset=38,
                                            value=Name(lineno=685, col_offset=38, id='np', ctx=Load()),
                                            attr='double',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='order',
                                        value=Str(lineno=685, col_offset=55, s='c'),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            lineno=686,
                            col_offset=8,
                            targets=[Name(lineno=686, col_offset=8, id='b', ctx=Store())],
                            value=Call(
                                lineno=686,
                                col_offset=12,
                                func=Attribute(
                                    lineno=686,
                                    col_offset=12,
                                    value=Name(lineno=686, col_offset=12, id='np', ctx=Load()),
                                    attr='asarray',
                                    ctx=Load(),
                                ),
                                args=[Name(lineno=686, col_offset=23, id='b', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='dtype',
                                        value=Attribute(
                                            lineno=686,
                                            col_offset=32,
                                            value=Name(lineno=686, col_offset=32, id='np', ctx=Load()),
                                            attr='double',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                If(
                    lineno=688,
                    col_offset=4,
                    test=Compare(
                        lineno=688,
                        col_offset=7,
                        left=Attribute(
                            lineno=688,
                            col_offset=7,
                            value=Name(lineno=688, col_offset=7, id='b', ctx=Load()),
                            attr='ndim',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Num(lineno=688, col_offset=17, n=1)],
                    ),
                    body=[
                        Assign(
                            lineno=689,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=689,
                                    col_offset=8,
                                    elts=[
                                        Name(lineno=689, col_offset=8, id='x', ctx=Store()),
                                        Name(lineno=689, col_offset=11, id='_', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=689,
                                col_offset=15,
                                func=Name(lineno=689, col_offset=15, id='levinson', ctx=Load()),
                                args=[
                                    Name(lineno=689, col_offset=24, id='vals', ctx=Load()),
                                    Call(
                                        lineno=689,
                                        col_offset=30,
                                        func=Attribute(
                                            lineno=689,
                                            col_offset=30,
                                            value=Name(lineno=689, col_offset=30, id='np', ctx=Load()),
                                            attr='ascontiguousarray',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=689, col_offset=51, id='b', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[
                        Assign(
                            lineno=691,
                            col_offset=8,
                            targets=[Name(lineno=691, col_offset=8, id='b_shape', ctx=Store())],
                            value=Attribute(
                                lineno=691,
                                col_offset=18,
                                value=Name(lineno=691, col_offset=18, id='b', ctx=Load()),
                                attr='shape',
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            lineno=692,
                            col_offset=8,
                            targets=[Name(lineno=692, col_offset=8, id='b', ctx=Store())],
                            value=Call(
                                lineno=692,
                                col_offset=12,
                                func=Attribute(
                                    lineno=692,
                                    col_offset=12,
                                    value=Name(lineno=692, col_offset=12, id='b', ctx=Load()),
                                    attr='reshape',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        lineno=692,
                                        col_offset=22,
                                        value=Attribute(
                                            lineno=692,
                                            col_offset=22,
                                            value=Name(lineno=692, col_offset=22, id='b', ctx=Load()),
                                            attr='shape',
                                            ctx=Load(),
                                        ),
                                        slice=Index(
                                            value=Num(lineno=692, col_offset=30, n=0),
                                        ),
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        lineno=692,
                                        col_offset=34,
                                        op=USub(),
                                        operand=Num(lineno=692, col_offset=35, n=1),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=693,
                            col_offset=8,
                            targets=[Name(lineno=693, col_offset=8, id='x', ctx=Store())],
                            value=Call(
                                lineno=693,
                                col_offset=12,
                                func=Attribute(
                                    lineno=693,
                                    col_offset=12,
                                    value=Name(lineno=693, col_offset=12, id='np', ctx=Load()),
                                    attr='column_stack',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        lineno=693,
                                        col_offset=29,
                                        elt=Subscript(
                                            lineno=693,
                                            col_offset=29,
                                            value=Call(
                                                lineno=693,
                                                col_offset=29,
                                                func=Name(lineno=693, col_offset=29, id='levinson', ctx=Load()),
                                                args=[
                                                    Name(lineno=693, col_offset=38, id='vals', ctx=Load()),
                                                    Call(
                                                        lineno=693,
                                                        col_offset=44,
                                                        func=Attribute(
                                                            lineno=693,
                                                            col_offset=44,
                                                            value=Name(lineno=693, col_offset=44, id='np', ctx=Load()),
                                                            attr='ascontiguousarray',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                lineno=693,
                                                                col_offset=65,
                                                                value=Name(lineno=693, col_offset=65, id='b', ctx=Load()),
                                                                slice=ExtSlice(
                                                                    dims=[
                                                                        Slice(lower=None, upper=None, step=None),
                                                                        Index(
                                                                            value=Name(lineno=693, col_offset=70, id='i', ctx=Load()),
                                                                        ),
                                                                    ],
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            slice=Index(
                                                value=Num(lineno=693, col_offset=75, n=0),
                                            ),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(lineno=694, col_offset=33, id='i', ctx=Store()),
                                                iter=Call(
                                                    lineno=694,
                                                    col_offset=38,
                                                    func=Name(lineno=694, col_offset=38, id='range', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            lineno=694,
                                                            col_offset=44,
                                                            value=Attribute(
                                                                lineno=694,
                                                                col_offset=44,
                                                                value=Name(lineno=694, col_offset=44, id='b', ctx=Load()),
                                                                attr='shape',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Index(
                                                                value=Num(lineno=694, col_offset=52, n=1),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=695,
                            col_offset=8,
                            targets=[Name(lineno=695, col_offset=8, id='x', ctx=Store())],
                            value=Call(
                                lineno=695,
                                col_offset=12,
                                func=Attribute(
                                    lineno=695,
                                    col_offset=12,
                                    value=Name(lineno=695, col_offset=12, id='x', ctx=Load()),
                                    attr='reshape',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        lineno=695,
                                        col_offset=22,
                                        value=Name(lineno=695, col_offset=23, id='b_shape', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                ),
                Return(
                    lineno=697,
                    col_offset=4,
                    value=Name(lineno=697, col_offset=11, id='x', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=700,
            col_offset=0,
            name='_get_axis_len',
            args=arguments(
                args=[
                    arg(lineno=700, col_offset=18, arg='aname', annotation=None),
                    arg(lineno=700, col_offset=25, arg='a', annotation=None),
                    arg(lineno=700, col_offset=28, arg='axis', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    lineno=701,
                    col_offset=4,
                    targets=[Name(lineno=701, col_offset=4, id='ax', ctx=Store())],
                    value=Name(lineno=701, col_offset=9, id='axis', ctx=Load()),
                ),
                If(
                    lineno=702,
                    col_offset=4,
                    test=Compare(
                        lineno=702,
                        col_offset=7,
                        left=Name(lineno=702, col_offset=7, id='ax', ctx=Load()),
                        ops=[Lt()],
                        comparators=[Num(lineno=702, col_offset=12, n=0)],
                    ),
                    body=[
                        AugAssign(
                            lineno=703,
                            col_offset=8,
                            target=Name(lineno=703, col_offset=8, id='ax', ctx=Store()),
                            op=Add(),
                            value=Attribute(
                                lineno=703,
                                col_offset=14,
                                value=Name(lineno=703, col_offset=14, id='a', ctx=Load()),
                                attr='ndim',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=704,
                    col_offset=4,
                    test=Compare(
                        lineno=704,
                        col_offset=7,
                        left=Num(lineno=704, col_offset=7, n=0),
                        ops=[
                            LtE(),
                            Lt(),
                        ],
                        comparators=[
                            Name(lineno=704, col_offset=12, id='ax', ctx=Load()),
                            Attribute(
                                lineno=704,
                                col_offset=17,
                                value=Name(lineno=704, col_offset=17, id='a', ctx=Load()),
                                attr='ndim',
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            lineno=705,
                            col_offset=8,
                            value=Subscript(
                                lineno=705,
                                col_offset=15,
                                value=Attribute(
                                    lineno=705,
                                    col_offset=15,
                                    value=Name(lineno=705, col_offset=15, id='a', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                                slice=Index(
                                    value=Name(lineno=705, col_offset=23, id='ax', ctx=Load()),
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Raise(
                    lineno=706,
                    col_offset=4,
                    exc=Call(
                        lineno=706,
                        col_offset=10,
                        func=Name(lineno=706, col_offset=10, id='ValueError', ctx=Load()),
                        args=[
                            BinOp(
                                lineno=706,
                                col_offset=21,
                                left=Str(lineno=706, col_offset=21, s="'%saxis' entry is out of bounds"),
                                op=Mod(),
                                right=Tuple(
                                    lineno=706,
                                    col_offset=58,
                                    elts=[Name(lineno=706, col_offset=58, id='aname', ctx=Load())],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                        keywords=[],
                    ),
                    cause=None,
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=709,
            col_offset=0,
            name='solve_circulant',
            args=arguments(
                args=[
                    arg(lineno=709, col_offset=20, arg='c', annotation=None),
                    arg(lineno=709, col_offset=23, arg='b', annotation=None),
                    arg(lineno=709, col_offset=26, arg='singular', annotation=None),
                    arg(lineno=709, col_offset=44, arg='tol', annotation=None),
                    arg(lineno=710, col_offset=20, arg='caxis', annotation=None),
                    arg(lineno=710, col_offset=30, arg='baxis', annotation=None),
                    arg(lineno=710, col_offset=39, arg='outaxis', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Str(lineno=709, col_offset=35, s='raise'),
                    NameConstant(lineno=709, col_offset=48, value=None),
                    UnaryOp(
                        lineno=710,
                        col_offset=26,
                        op=USub(),
                        operand=Num(lineno=710, col_offset=27, n=1),
                    ),
                    Num(lineno=710, col_offset=36, n=0),
                    Num(lineno=710, col_offset=47, n=0),
                ],
            ),
            body=[
                Expr(
                    lineno=856,
                    col_offset=-1,
                    value=Str(lineno=856, col_offset=-1, s='Solve C x = b for x, where C is a circulant matrix.\n\n    `C` is the circulant matrix associated with the vector `c`.\n\n    The system is solved by doing division in Fourier space.  The\n    calculation is::\n\n        x = ifft(fft(b) / fft(c))\n\n    where `fft` and `ifft` are the fast Fourier transform and its inverse,\n    respectively.  For a large vector `c`, this is *much* faster than\n    solving the system with the full circulant matrix.\n\n    Parameters\n    ----------\n    c : array_like\n        The coefficients of the circulant matrix.\n    b : array_like\n        Right-hand side matrix in ``a x = b``.\n    singular : str, optional\n        This argument controls how a near singular circulant matrix is\n        handled.  If `singular` is "raise" and the circulant matrix is\n        near singular, a `LinAlgError` is raised.  If `singular` is\n        "lstsq", the least squares solution is returned.  Default is "raise".\n    tol : float, optional\n        If any eigenvalue of the circulant matrix has an absolute value\n        that is less than or equal to `tol`, the matrix is considered to be\n        near singular.  If not given, `tol` is set to::\n\n            tol = abs_eigs.max() * abs_eigs.size * np.finfo(np.float64).eps\n\n        where `abs_eigs` is the array of absolute values of the eigenvalues\n        of the circulant matrix.\n    caxis : int\n        When `c` has dimension greater than 1, it is viewed as a collection\n        of circulant vectors.  In this case, `caxis` is the axis of `c` that\n        holds the vectors of circulant coefficients.\n    baxis : int\n        When `b` has dimension greater than 1, it is viewed as a collection\n        of vectors.  In this case, `baxis` is the axis of `b` that holds the\n        right-hand side vectors.\n    outaxis : int\n        When `c` or `b` are multidimensional, the value returned by\n        `solve_circulant` is multidimensional.  In this case, `outaxis` is\n        the axis of the result that holds the solution vectors.\n\n    Returns\n    -------\n    x : ndarray\n        Solution to the system ``C x = b``.\n\n    Raises\n    ------\n    LinAlgError\n        If the circulant matrix associated with `c` is near singular.\n\n    See Also\n    --------\n    circulant : circulant matrix\n\n    Notes\n    -----\n    For a one-dimensional vector `c` with length `m`, and an array `b`\n    with shape ``(m, ...)``,\n\n        solve_circulant(c, b)\n\n    returns the same result as\n\n        solve(circulant(c), b)\n\n    where `solve` and `circulant` are from `scipy.linalg`.\n\n    .. versionadded:: 0.16.0\n\n    Examples\n    --------\n    >>> from scipy.linalg import solve_circulant, solve, circulant, lstsq\n\n    >>> c = np.array([2, 2, 4])\n    >>> b = np.array([1, 2, 3])\n    >>> solve_circulant(c, b)\n    array([ 0.75, -0.25,  0.25])\n\n    Compare that result to solving the system with `scipy.linalg.solve`:\n\n    >>> solve(circulant(c), b)\n    array([ 0.75, -0.25,  0.25])\n\n    A singular example:\n\n    >>> c = np.array([1, 1, 0, 0])\n    >>> b = np.array([1, 2, 3, 4])\n\n    Calling ``solve_circulant(c, b)`` will raise a `LinAlgError`.  For the\n    least square solution, use the option ``singular=\'lstsq\'``:\n\n    >>> solve_circulant(c, b, singular=\'lstsq\')\n    array([ 0.25,  1.25,  2.25,  1.25])\n\n    Compare to `scipy.linalg.lstsq`:\n\n    >>> x, resid, rnk, s = lstsq(circulant(c), b)\n    >>> x\n    array([ 0.25,  1.25,  2.25,  1.25])\n\n    A broadcasting example:\n\n    Suppose we have the vectors of two circulant matrices stored in an array\n    with shape (2, 5), and three `b` vectors stored in an array with shape\n    (3, 5).  For example,\n\n    >>> c = np.array([[1.5, 2, 3, 0, 0], [1, 1, 4, 3, 2]])\n    >>> b = np.arange(15).reshape(-1, 5)\n\n    We want to solve all combinations of circulant matrices and `b` vectors,\n    with the result stored in an array with shape (2, 3, 5).  When we\n    disregard the axes of `c` and `b` that hold the vectors of coefficients,\n    the shapes of the collections are (2,) and (3,), respectively, which are\n    not compatible for broadcasting.  To have a broadcast result with shape\n    (2, 3), we add a trivial dimension to `c`: ``c[:, np.newaxis, :]`` has\n    shape (2, 1, 5).  The last dimension holds the coefficients of the\n    circulant matrices, so when we call `solve_circulant`, we can use the\n    default ``caxis=-1``.  The coefficients of the `b` vectors are in the last\n    dimension of the array `b`, so we use ``baxis=-1``.  If we use the\n    default `outaxis`, the result will have shape (5, 2, 3), so we\'ll use\n    ``outaxis=-1`` to put the solution vectors in the last dimension.\n\n    >>> x = solve_circulant(c[:, np.newaxis, :], b, baxis=-1, outaxis=-1)\n    >>> x.shape\n    (2, 3, 5)\n    >>> np.set_printoptions(precision=3)  # For compact output of numbers.\n    >>> x\n    array([[[-0.118,  0.22 ,  1.277, -0.142,  0.302],\n            [ 0.651,  0.989,  2.046,  0.627,  1.072],\n            [ 1.42 ,  1.758,  2.816,  1.396,  1.841]],\n           [[ 0.401,  0.304,  0.694, -0.867,  0.377],\n            [ 0.856,  0.758,  1.149, -0.412,  0.831],\n            [ 1.31 ,  1.213,  1.603,  0.042,  1.286]]])\n\n    Check by solving one pair of `c` and `b` vectors (cf. ``x[1, 1, :]``):\n\n    >>> solve_circulant(c[1], b[1, :])\n    array([ 0.856,  0.758,  1.149, -0.412,  0.831])\n\n    '),
                ),
                Assign(
                    lineno=857,
                    col_offset=4,
                    targets=[Name(lineno=857, col_offset=4, id='c', ctx=Store())],
                    value=Call(
                        lineno=857,
                        col_offset=8,
                        func=Attribute(
                            lineno=857,
                            col_offset=8,
                            value=Name(lineno=857, col_offset=8, id='np', ctx=Load()),
                            attr='atleast_1d',
                            ctx=Load(),
                        ),
                        args=[Name(lineno=857, col_offset=22, id='c', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=858,
                    col_offset=4,
                    targets=[Name(lineno=858, col_offset=4, id='nc', ctx=Store())],
                    value=Call(
                        lineno=858,
                        col_offset=9,
                        func=Name(lineno=858, col_offset=9, id='_get_axis_len', ctx=Load()),
                        args=[
                            Str(lineno=858, col_offset=23, s='c'),
                            Name(lineno=858, col_offset=28, id='c', ctx=Load()),
                            Name(lineno=858, col_offset=31, id='caxis', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=859,
                    col_offset=4,
                    targets=[Name(lineno=859, col_offset=4, id='b', ctx=Store())],
                    value=Call(
                        lineno=859,
                        col_offset=8,
                        func=Attribute(
                            lineno=859,
                            col_offset=8,
                            value=Name(lineno=859, col_offset=8, id='np', ctx=Load()),
                            attr='atleast_1d',
                            ctx=Load(),
                        ),
                        args=[Name(lineno=859, col_offset=22, id='b', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=860,
                    col_offset=4,
                    targets=[Name(lineno=860, col_offset=4, id='nb', ctx=Store())],
                    value=Call(
                        lineno=860,
                        col_offset=9,
                        func=Name(lineno=860, col_offset=9, id='_get_axis_len', ctx=Load()),
                        args=[
                            Str(lineno=860, col_offset=23, s='b'),
                            Name(lineno=860, col_offset=28, id='b', ctx=Load()),
                            Name(lineno=860, col_offset=31, id='baxis', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=861,
                    col_offset=4,
                    test=Compare(
                        lineno=861,
                        col_offset=7,
                        left=Name(lineno=861, col_offset=7, id='nc', ctx=Load()),
                        ops=[NotEq()],
                        comparators=[Name(lineno=861, col_offset=13, id='nb', ctx=Load())],
                    ),
                    body=[
                        Raise(
                            lineno=862,
                            col_offset=8,
                            exc=Call(
                                lineno=862,
                                col_offset=14,
                                func=Name(lineno=862, col_offset=14, id='ValueError', ctx=Load()),
                                args=[Str(lineno=862, col_offset=25, s='Incompatible c and b axis lengths')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=864,
                    col_offset=4,
                    targets=[Name(lineno=864, col_offset=4, id='fc', ctx=Store())],
                    value=Call(
                        lineno=864,
                        col_offset=9,
                        func=Attribute(
                            lineno=864,
                            col_offset=9,
                            value=Attribute(
                                lineno=864,
                                col_offset=9,
                                value=Name(lineno=864, col_offset=9, id='np', ctx=Load()),
                                attr='fft',
                                ctx=Load(),
                            ),
                            attr='fft',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                lineno=864,
                                col_offset=20,
                                func=Attribute(
                                    lineno=864,
                                    col_offset=20,
                                    value=Name(lineno=864, col_offset=20, id='np', ctx=Load()),
                                    attr='rollaxis',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=864, col_offset=32, id='c', ctx=Load()),
                                    Name(lineno=864, col_offset=35, id='caxis', ctx=Load()),
                                    Attribute(
                                        lineno=864,
                                        col_offset=42,
                                        value=Name(lineno=864, col_offset=42, id='c', ctx=Load()),
                                        attr='ndim',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='axis',
                                value=UnaryOp(
                                    lineno=864,
                                    col_offset=56,
                                    op=USub(),
                                    operand=Num(lineno=864, col_offset=57, n=1),
                                ),
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=865,
                    col_offset=4,
                    targets=[Name(lineno=865, col_offset=4, id='abs_fc', ctx=Store())],
                    value=Call(
                        lineno=865,
                        col_offset=13,
                        func=Attribute(
                            lineno=865,
                            col_offset=13,
                            value=Name(lineno=865, col_offset=13, id='np', ctx=Load()),
                            attr='abs',
                            ctx=Load(),
                        ),
                        args=[Name(lineno=865, col_offset=20, id='fc', ctx=Load())],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=866,
                    col_offset=4,
                    test=Compare(
                        lineno=866,
                        col_offset=7,
                        left=Name(lineno=866, col_offset=7, id='tol', ctx=Load()),
                        ops=[Is()],
                        comparators=[NameConstant(lineno=866, col_offset=14, value=None)],
                    ),
                    body=[
                        Assign(
                            lineno=868,
                            col_offset=8,
                            targets=[Name(lineno=868, col_offset=8, id='tol', ctx=Store())],
                            value=BinOp(
                                lineno=868,
                                col_offset=39,
                                left=BinOp(
                                    lineno=868,
                                    col_offset=14,
                                    left=Call(
                                        lineno=868,
                                        col_offset=14,
                                        func=Attribute(
                                            lineno=868,
                                            col_offset=14,
                                            value=Name(lineno=868, col_offset=14, id='abs_fc', ctx=Load()),
                                            attr='max',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='axis',
                                                value=UnaryOp(
                                                    lineno=868,
                                                    col_offset=30,
                                                    op=USub(),
                                                    operand=Num(lineno=868, col_offset=31, n=1),
                                                ),
                                            ),
                                        ],
                                    ),
                                    op=Mult(),
                                    right=Name(lineno=868, col_offset=36, id='nc', ctx=Load()),
                                ),
                                op=Mult(),
                                right=Attribute(
                                    lineno=868,
                                    col_offset=41,
                                    value=Call(
                                        lineno=868,
                                        col_offset=41,
                                        func=Attribute(
                                            lineno=868,
                                            col_offset=41,
                                            value=Name(lineno=868, col_offset=41, id='np', ctx=Load()),
                                            attr='finfo',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                lineno=868,
                                                col_offset=50,
                                                value=Name(lineno=868, col_offset=50, id='np', ctx=Load()),
                                                attr='float64',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='eps',
                                    ctx=Load(),
                                ),
                            ),
                        ),
                        If(
                            lineno=869,
                            col_offset=8,
                            test=Compare(
                                lineno=869,
                                col_offset=11,
                                left=Attribute(
                                    lineno=869,
                                    col_offset=11,
                                    value=Name(lineno=869, col_offset=11, id='tol', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Tuple(lineno=869, col_offset=24, elts=[], ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    lineno=870,
                                    col_offset=12,
                                    targets=[
                                        Attribute(
                                            lineno=870,
                                            col_offset=12,
                                            value=Name(lineno=870, col_offset=12, id='tol', ctx=Load()),
                                            attr='shape',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        lineno=870,
                                        col_offset=24,
                                        left=Attribute(
                                            lineno=870,
                                            col_offset=24,
                                            value=Name(lineno=870, col_offset=24, id='tol', ctx=Load()),
                                            attr='shape',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Tuple(
                                            lineno=870,
                                            col_offset=37,
                                            elts=[Num(lineno=870, col_offset=37, n=1)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    lineno=872,
                                    col_offset=12,
                                    targets=[Name(lineno=872, col_offset=12, id='tol', ctx=Store())],
                                    value=Call(
                                        lineno=872,
                                        col_offset=18,
                                        func=Attribute(
                                            lineno=872,
                                            col_offset=18,
                                            value=Name(lineno=872, col_offset=18, id='np', ctx=Load()),
                                            attr='atleast_1d',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=872, col_offset=32, id='tol', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=874,
                    col_offset=4,
                    targets=[Name(lineno=874, col_offset=4, id='near_zeros', ctx=Store())],
                    value=Compare(
                        lineno=874,
                        col_offset=17,
                        left=Name(lineno=874, col_offset=17, id='abs_fc', ctx=Load()),
                        ops=[LtE()],
                        comparators=[Name(lineno=874, col_offset=27, id='tol', ctx=Load())],
                    ),
                ),
                Assign(
                    lineno=875,
                    col_offset=4,
                    targets=[Name(lineno=875, col_offset=4, id='is_near_singular', ctx=Store())],
                    value=Call(
                        lineno=875,
                        col_offset=23,
                        func=Attribute(
                            lineno=875,
                            col_offset=23,
                            value=Name(lineno=875, col_offset=23, id='np', ctx=Load()),
                            attr='any',
                            ctx=Load(),
                        ),
                        args=[Name(lineno=875, col_offset=30, id='near_zeros', ctx=Load())],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=876,
                    col_offset=4,
                    test=Name(lineno=876, col_offset=7, id='is_near_singular', ctx=Load()),
                    body=[
                        If(
                            lineno=877,
                            col_offset=8,
                            test=Compare(
                                lineno=877,
                                col_offset=11,
                                left=Name(lineno=877, col_offset=11, id='singular', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Str(lineno=877, col_offset=23, s='raise')],
                            ),
                            body=[
                                Raise(
                                    lineno=878,
                                    col_offset=12,
                                    exc=Call(
                                        lineno=878,
                                        col_offset=18,
                                        func=Name(lineno=878, col_offset=18, id='LinAlgError', ctx=Load()),
                                        args=[Str(lineno=878, col_offset=30, s='near singular circulant matrix.')],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    lineno=882,
                                    col_offset=12,
                                    targets=[
                                        Subscript(
                                            lineno=882,
                                            col_offset=12,
                                            value=Name(lineno=882, col_offset=12, id='fc', ctx=Load()),
                                            slice=Index(
                                                value=Name(lineno=882, col_offset=15, id='near_zeros', ctx=Load()),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Num(lineno=882, col_offset=29, n=1),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=884,
                    col_offset=4,
                    targets=[Name(lineno=884, col_offset=4, id='fb', ctx=Store())],
                    value=Call(
                        lineno=884,
                        col_offset=9,
                        func=Attribute(
                            lineno=884,
                            col_offset=9,
                            value=Attribute(
                                lineno=884,
                                col_offset=9,
                                value=Name(lineno=884, col_offset=9, id='np', ctx=Load()),
                                attr='fft',
                                ctx=Load(),
                            ),
                            attr='fft',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                lineno=884,
                                col_offset=20,
                                func=Attribute(
                                    lineno=884,
                                    col_offset=20,
                                    value=Name(lineno=884, col_offset=20, id='np', ctx=Load()),
                                    attr='rollaxis',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=884, col_offset=32, id='b', ctx=Load()),
                                    Name(lineno=884, col_offset=35, id='baxis', ctx=Load()),
                                    Attribute(
                                        lineno=884,
                                        col_offset=42,
                                        value=Name(lineno=884, col_offset=42, id='b', ctx=Load()),
                                        attr='ndim',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='axis',
                                value=UnaryOp(
                                    lineno=884,
                                    col_offset=56,
                                    op=USub(),
                                    operand=Num(lineno=884, col_offset=57, n=1),
                                ),
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=886,
                    col_offset=4,
                    targets=[Name(lineno=886, col_offset=4, id='q', ctx=Store())],
                    value=BinOp(
                        lineno=886,
                        col_offset=8,
                        left=Name(lineno=886, col_offset=8, id='fb', ctx=Load()),
                        op=Div(),
                        right=Name(lineno=886, col_offset=13, id='fc', ctx=Load()),
                    ),
                ),
                If(
                    lineno=888,
                    col_offset=4,
                    test=Name(lineno=888, col_offset=7, id='is_near_singular', ctx=Load()),
                    body=[
                        Assign(
                            lineno=894,
                            col_offset=8,
                            targets=[Name(lineno=894, col_offset=8, id='mask', ctx=Store())],
                            value=BinOp(
                                lineno=894,
                                col_offset=15,
                                left=Call(
                                    lineno=894,
                                    col_offset=15,
                                    func=Attribute(
                                        lineno=894,
                                        col_offset=15,
                                        value=Name(lineno=894, col_offset=15, id='np', ctx=Load()),
                                        attr='ones_like',
                                        ctx=Load(),
                                    ),
                                    args=[Name(lineno=894, col_offset=28, id='b', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='dtype',
                                            value=Name(lineno=894, col_offset=37, id='bool', ctx=Load()),
                                        ),
                                    ],
                                ),
                                op=BitAnd(),
                                right=Name(lineno=894, col_offset=45, id='near_zeros', ctx=Load()),
                            ),
                        ),
                        Assign(
                            lineno=895,
                            col_offset=8,
                            targets=[
                                Subscript(
                                    lineno=895,
                                    col_offset=8,
                                    value=Name(lineno=895, col_offset=8, id='q', ctx=Load()),
                                    slice=Index(
                                        value=Name(lineno=895, col_offset=10, id='mask', ctx=Load()),
                                    ),
                                    ctx=Store(),
                                ),
                            ],
                            value=Num(lineno=895, col_offset=18, n=0),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=897,
                    col_offset=4,
                    targets=[Name(lineno=897, col_offset=4, id='x', ctx=Store())],
                    value=Call(
                        lineno=897,
                        col_offset=8,
                        func=Attribute(
                            lineno=897,
                            col_offset=8,
                            value=Attribute(
                                lineno=897,
                                col_offset=8,
                                value=Name(lineno=897, col_offset=8, id='np', ctx=Load()),
                                attr='fft',
                                ctx=Load(),
                            ),
                            attr='ifft',
                            ctx=Load(),
                        ),
                        args=[Name(lineno=897, col_offset=20, id='q', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='axis',
                                value=UnaryOp(
                                    lineno=897,
                                    col_offset=28,
                                    op=USub(),
                                    operand=Num(lineno=897, col_offset=29, n=1),
                                ),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=898,
                    col_offset=4,
                    test=UnaryOp(
                        lineno=898,
                        col_offset=7,
                        op=Not(),
                        operand=BoolOp(
                            lineno=898,
                            col_offset=12,
                            op=Or(),
                            values=[
                                Call(
                                    lineno=898,
                                    col_offset=12,
                                    func=Attribute(
                                        lineno=898,
                                        col_offset=12,
                                        value=Name(lineno=898, col_offset=12, id='np', ctx=Load()),
                                        attr='iscomplexobj',
                                        ctx=Load(),
                                    ),
                                    args=[Name(lineno=898, col_offset=28, id='c', ctx=Load())],
                                    keywords=[],
                                ),
                                Call(
                                    lineno=898,
                                    col_offset=34,
                                    func=Attribute(
                                        lineno=898,
                                        col_offset=34,
                                        value=Name(lineno=898, col_offset=34, id='np', ctx=Load()),
                                        attr='iscomplexobj',
                                        ctx=Load(),
                                    ),
                                    args=[Name(lineno=898, col_offset=50, id='b', ctx=Load())],
                                    keywords=[],
                                ),
                            ],
                        ),
                    ),
                    body=[
                        Assign(
                            lineno=899,
                            col_offset=8,
                            targets=[Name(lineno=899, col_offset=8, id='x', ctx=Store())],
                            value=Attribute(
                                lineno=899,
                                col_offset=12,
                                value=Name(lineno=899, col_offset=12, id='x', ctx=Load()),
                                attr='real',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=900,
                    col_offset=4,
                    test=Compare(
                        lineno=900,
                        col_offset=7,
                        left=Name(lineno=900, col_offset=7, id='outaxis', ctx=Load()),
                        ops=[NotEq()],
                        comparators=[
                            UnaryOp(
                                lineno=900,
                                col_offset=18,
                                op=USub(),
                                operand=Num(lineno=900, col_offset=19, n=1),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            lineno=901,
                            col_offset=8,
                            targets=[Name(lineno=901, col_offset=8, id='x', ctx=Store())],
                            value=Call(
                                lineno=901,
                                col_offset=12,
                                func=Attribute(
                                    lineno=901,
                                    col_offset=12,
                                    value=Name(lineno=901, col_offset=12, id='np', ctx=Load()),
                                    attr='rollaxis',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(lineno=901, col_offset=24, id='x', ctx=Load()),
                                    UnaryOp(
                                        lineno=901,
                                        col_offset=27,
                                        op=USub(),
                                        operand=Num(lineno=901, col_offset=28, n=1),
                                    ),
                                    Name(lineno=901, col_offset=31, id='outaxis', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    lineno=902,
                    col_offset=4,
                    value=Name(lineno=902, col_offset=11, id='x', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=906,
            col_offset=0,
            name='inv',
            args=arguments(
                args=[
                    arg(lineno=906, col_offset=8, arg='a', annotation=None),
                    arg(lineno=906, col_offset=11, arg='overwrite_a', annotation=None),
                    arg(lineno=906, col_offset=30, arg='check_finite', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    NameConstant(lineno=906, col_offset=23, value=False),
                    NameConstant(lineno=906, col_offset=43, value=True),
                ],
            ),
            body=[
                Expr(
                    lineno=944,
                    col_offset=-1,
                    value=Str(lineno=944, col_offset=-1, s='\n    Compute the inverse of a matrix.\n\n    Parameters\n    ----------\n    a : array_like\n        Square matrix to be inverted.\n    overwrite_a : bool, optional\n        Discard data in `a` (may improve performance). Default is False.\n    check_finite : bool, optional\n        Whether to check that the input matrix contains only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n\n    Returns\n    -------\n    ainv : ndarray\n        Inverse of the matrix `a`.\n\n    Raises\n    ------\n    LinAlgError\n        If `a` is singular.\n    ValueError\n        If `a` is not square, or not 2-dimensional.\n\n    Examples\n    --------\n    >>> from scipy import linalg\n    >>> a = np.array([[1., 2.], [3., 4.]])\n    >>> linalg.inv(a)\n    array([[-2. ,  1. ],\n           [ 1.5, -0.5]])\n    >>> np.dot(a, linalg.inv(a))\n    array([[ 1.,  0.],\n           [ 0.,  1.]])\n\n    '),
                ),
                Assign(
                    lineno=945,
                    col_offset=4,
                    targets=[Name(lineno=945, col_offset=4, id='a1', ctx=Store())],
                    value=Call(
                        lineno=945,
                        col_offset=9,
                        func=Name(lineno=945, col_offset=9, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=945, col_offset=28, id='a', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=945, col_offset=44, id='check_finite', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=946,
                    col_offset=4,
                    test=BoolOp(
                        lineno=946,
                        col_offset=7,
                        op=Or(),
                        values=[
                            Compare(
                                lineno=946,
                                col_offset=7,
                                left=Call(
                                    lineno=946,
                                    col_offset=7,
                                    func=Name(lineno=946, col_offset=7, id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            lineno=946,
                                            col_offset=11,
                                            value=Name(lineno=946, col_offset=11, id='a1', ctx=Load()),
                                            attr='shape',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Num(lineno=946, col_offset=24, n=2)],
                            ),
                            Compare(
                                lineno=946,
                                col_offset=29,
                                left=Subscript(
                                    lineno=946,
                                    col_offset=29,
                                    value=Attribute(
                                        lineno=946,
                                        col_offset=29,
                                        value=Name(lineno=946, col_offset=29, id='a1', ctx=Load()),
                                        attr='shape',
                                        ctx=Load(),
                                    ),
                                    slice=Index(
                                        value=Num(lineno=946, col_offset=38, n=0),
                                    ),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Subscript(
                                        lineno=946,
                                        col_offset=44,
                                        value=Attribute(
                                            lineno=946,
                                            col_offset=44,
                                            value=Name(lineno=946, col_offset=44, id='a1', ctx=Load()),
                                            attr='shape',
                                            ctx=Load(),
                                        ),
                                        slice=Index(
                                            value=Num(lineno=946, col_offset=53, n=1),
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            lineno=947,
                            col_offset=8,
                            exc=Call(
                                lineno=947,
                                col_offset=14,
                                func=Name(lineno=947, col_offset=14, id='ValueError', ctx=Load()),
                                args=[Str(lineno=947, col_offset=25, s='expected square matrix')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=948,
                    col_offset=4,
                    targets=[Name(lineno=948, col_offset=4, id='overwrite_a', ctx=Store())],
                    value=BoolOp(
                        lineno=948,
                        col_offset=18,
                        op=Or(),
                        values=[
                            Name(lineno=948, col_offset=18, id='overwrite_a', ctx=Load()),
                            Call(
                                lineno=948,
                                col_offset=33,
                                func=Name(lineno=948, col_offset=33, id='_datacopied', ctx=Load()),
                                args=[
                                    Name(lineno=948, col_offset=45, id='a1', ctx=Load()),
                                    Name(lineno=948, col_offset=49, id='a', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=958,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=958,
                            col_offset=4,
                            elts=[
                                Name(lineno=958, col_offset=4, id='getrf', ctx=Store()),
                                Name(lineno=958, col_offset=11, id='getri', ctx=Store()),
                                Name(lineno=958, col_offset=18, id='getri_lwork', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        lineno=958,
                        col_offset=32,
                        func=Name(lineno=958, col_offset=32, id='get_lapack_funcs', ctx=Load()),
                        args=[
                            Tuple(
                                lineno=958,
                                col_offset=50,
                                elts=[
                                    Str(lineno=958, col_offset=50, s='getrf'),
                                    Str(lineno=958, col_offset=59, s='getri'),
                                    Str(lineno=959, col_offset=50, s='getri_lwork'),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                lineno=960,
                                col_offset=50,
                                elts=[Name(lineno=960, col_offset=50, id='a1', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=961,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=961,
                            col_offset=4,
                            elts=[
                                Name(lineno=961, col_offset=4, id='lu', ctx=Store()),
                                Name(lineno=961, col_offset=8, id='piv', ctx=Store()),
                                Name(lineno=961, col_offset=13, id='info', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        lineno=961,
                        col_offset=20,
                        func=Name(lineno=961, col_offset=20, id='getrf', ctx=Load()),
                        args=[Name(lineno=961, col_offset=26, id='a1', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='overwrite_a',
                                value=Name(lineno=961, col_offset=42, id='overwrite_a', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=962,
                    col_offset=4,
                    test=Compare(
                        lineno=962,
                        col_offset=7,
                        left=Name(lineno=962, col_offset=7, id='info', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Num(lineno=962, col_offset=15, n=0)],
                    ),
                    body=[
                        Assign(
                            lineno=963,
                            col_offset=8,
                            targets=[Name(lineno=963, col_offset=8, id='lwork', ctx=Store())],
                            value=Call(
                                lineno=963,
                                col_offset=16,
                                func=Name(lineno=963, col_offset=16, id='_compute_lwork', ctx=Load()),
                                args=[
                                    Name(lineno=963, col_offset=31, id='getri_lwork', ctx=Load()),
                                    Subscript(
                                        lineno=963,
                                        col_offset=44,
                                        value=Attribute(
                                            lineno=963,
                                            col_offset=44,
                                            value=Name(lineno=963, col_offset=44, id='a1', ctx=Load()),
                                            attr='shape',
                                            ctx=Load(),
                                        ),
                                        slice=Index(
                                            value=Num(lineno=963, col_offset=53, n=0),
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=971,
                            col_offset=8,
                            targets=[Name(lineno=971, col_offset=8, id='lwork', ctx=Store())],
                            value=Call(
                                lineno=971,
                                col_offset=16,
                                func=Name(lineno=971, col_offset=16, id='int', ctx=Load()),
                                args=[
                                    BinOp(
                                        lineno=971,
                                        col_offset=20,
                                        left=Num(lineno=971, col_offset=20, n=1.01),
                                        op=Mult(),
                                        right=Name(lineno=971, col_offset=27, id='lwork', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=972,
                            col_offset=8,
                            targets=[
                                Tuple(
                                    lineno=972,
                                    col_offset=8,
                                    elts=[
                                        Name(lineno=972, col_offset=8, id='inv_a', ctx=Store()),
                                        Name(lineno=972, col_offset=15, id='info', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                lineno=972,
                                col_offset=22,
                                func=Name(lineno=972, col_offset=22, id='getri', ctx=Load()),
                                args=[
                                    Name(lineno=972, col_offset=28, id='lu', ctx=Load()),
                                    Name(lineno=972, col_offset=32, id='piv', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='lwork',
                                        value=Name(lineno=972, col_offset=43, id='lwork', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='overwrite_lu',
                                        value=Num(lineno=972, col_offset=63, n=1),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=973,
                    col_offset=4,
                    test=Compare(
                        lineno=973,
                        col_offset=7,
                        left=Name(lineno=973, col_offset=7, id='info', ctx=Load()),
                        ops=[Gt()],
                        comparators=[Num(lineno=973, col_offset=14, n=0)],
                    ),
                    body=[
                        Raise(
                            lineno=974,
                            col_offset=8,
                            exc=Call(
                                lineno=974,
                                col_offset=14,
                                func=Name(lineno=974, col_offset=14, id='LinAlgError', ctx=Load()),
                                args=[Str(lineno=974, col_offset=26, s='singular matrix')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=975,
                    col_offset=4,
                    test=Compare(
                        lineno=975,
                        col_offset=7,
                        left=Name(lineno=975, col_offset=7, id='info', ctx=Load()),
                        ops=[Lt()],
                        comparators=[Num(lineno=975, col_offset=14, n=0)],
                    ),
                    body=[
                        Raise(
                            lineno=976,
                            col_offset=8,
                            exc=Call(
                                lineno=976,
                                col_offset=14,
                                func=Name(lineno=976, col_offset=14, id='ValueError', ctx=Load()),
                                args=[
                                    BinOp(
                                        lineno=976,
                                        col_offset=25,
                                        left=Str(lineno=976, col_offset=25, s='illegal value in %d-th argument of internal getrf|getri'),
                                        op=Mod(),
                                        right=UnaryOp(
                                            lineno=977,
                                            col_offset=41,
                                            op=USub(),
                                            operand=Name(lineno=977, col_offset=42, id='info', ctx=Load()),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    lineno=978,
                    col_offset=4,
                    value=Name(lineno=978, col_offset=11, id='inv_a', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=983,
            col_offset=0,
            name='det',
            args=arguments(
                args=[
                    arg(lineno=983, col_offset=8, arg='a', annotation=None),
                    arg(lineno=983, col_offset=11, arg='overwrite_a', annotation=None),
                    arg(lineno=983, col_offset=30, arg='check_finite', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    NameConstant(lineno=983, col_offset=23, value=False),
                    NameConstant(lineno=983, col_offset=43, value=True),
                ],
            ),
            body=[
                Expr(
                    lineno=1028,
                    col_offset=-1,
                    value=Str(lineno=1028, col_offset=-1, s='\n    Compute the determinant of a matrix\n\n    The determinant of a square matrix is a value derived arithmetically\n    from the coefficients of the matrix.\n\n    The determinant for a 3x3 matrix, for example, is computed as follows::\n\n        a    b    c\n        d    e    f = A\n        g    h    i\n\n        det(A) = a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h\n\n    Parameters\n    ----------\n    a : (M, M) array_like\n        A square matrix.\n    overwrite_a : bool, optional\n        Allow overwriting data in a (may enhance performance).\n    check_finite : bool, optional\n        Whether to check that the input matrix contains only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n\n    Returns\n    -------\n    det : float or complex\n        Determinant of `a`.\n\n    Notes\n    -----\n    The determinant is computed via LU factorization, LAPACK routine z/dgetrf.\n\n    Examples\n    --------\n    >>> from scipy import linalg\n    >>> a = np.array([[1,2,3], [4,5,6], [7,8,9]])\n    >>> linalg.det(a)\n    0.0\n    >>> a = np.array([[0,2,3], [4,5,6], [7,8,9]])\n    >>> linalg.det(a)\n    3.0\n\n    '),
                ),
                Assign(
                    lineno=1029,
                    col_offset=4,
                    targets=[Name(lineno=1029, col_offset=4, id='a1', ctx=Store())],
                    value=Call(
                        lineno=1029,
                        col_offset=9,
                        func=Name(lineno=1029, col_offset=9, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=1029, col_offset=28, id='a', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=1029, col_offset=44, id='check_finite', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=1030,
                    col_offset=4,
                    test=BoolOp(
                        lineno=1030,
                        col_offset=7,
                        op=Or(),
                        values=[
                            Compare(
                                lineno=1030,
                                col_offset=7,
                                left=Call(
                                    lineno=1030,
                                    col_offset=7,
                                    func=Name(lineno=1030, col_offset=7, id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            lineno=1030,
                                            col_offset=11,
                                            value=Name(lineno=1030, col_offset=11, id='a1', ctx=Load()),
                                            attr='shape',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Num(lineno=1030, col_offset=24, n=2)],
                            ),
                            Compare(
                                lineno=1030,
                                col_offset=29,
                                left=Subscript(
                                    lineno=1030,
                                    col_offset=29,
                                    value=Attribute(
                                        lineno=1030,
                                        col_offset=29,
                                        value=Name(lineno=1030, col_offset=29, id='a1', ctx=Load()),
                                        attr='shape',
                                        ctx=Load(),
                                    ),
                                    slice=Index(
                                        value=Num(lineno=1030, col_offset=38, n=0),
                                    ),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Subscript(
                                        lineno=1030,
                                        col_offset=44,
                                        value=Attribute(
                                            lineno=1030,
                                            col_offset=44,
                                            value=Name(lineno=1030, col_offset=44, id='a1', ctx=Load()),
                                            attr='shape',
                                            ctx=Load(),
                                        ),
                                        slice=Index(
                                            value=Num(lineno=1030, col_offset=53, n=1),
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            lineno=1031,
                            col_offset=8,
                            exc=Call(
                                lineno=1031,
                                col_offset=14,
                                func=Name(lineno=1031, col_offset=14, id='ValueError', ctx=Load()),
                                args=[Str(lineno=1031, col_offset=25, s='expected square matrix')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=1032,
                    col_offset=4,
                    targets=[Name(lineno=1032, col_offset=4, id='overwrite_a', ctx=Store())],
                    value=BoolOp(
                        lineno=1032,
                        col_offset=18,
                        op=Or(),
                        values=[
                            Name(lineno=1032, col_offset=18, id='overwrite_a', ctx=Load()),
                            Call(
                                lineno=1032,
                                col_offset=33,
                                func=Name(lineno=1032, col_offset=33, id='_datacopied', ctx=Load()),
                                args=[
                                    Name(lineno=1032, col_offset=45, id='a1', ctx=Load()),
                                    Name(lineno=1032, col_offset=49, id='a', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=1033,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=1033,
                            col_offset=4,
                            elts=[Name(lineno=1033, col_offset=4, id='fdet', ctx=Store())],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        lineno=1033,
                        col_offset=12,
                        func=Name(lineno=1033, col_offset=12, id='get_flinalg_funcs', ctx=Load()),
                        args=[
                            Tuple(
                                lineno=1033,
                                col_offset=31,
                                elts=[Str(lineno=1033, col_offset=31, s='det')],
                                ctx=Load(),
                            ),
                            Tuple(
                                lineno=1033,
                                col_offset=41,
                                elts=[Name(lineno=1033, col_offset=41, id='a1', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=1034,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=1034,
                            col_offset=4,
                            elts=[
                                Name(lineno=1034, col_offset=4, id='a_det', ctx=Store()),
                                Name(lineno=1034, col_offset=11, id='info', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        lineno=1034,
                        col_offset=18,
                        func=Name(lineno=1034, col_offset=18, id='fdet', ctx=Load()),
                        args=[Name(lineno=1034, col_offset=23, id='a1', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='overwrite_a',
                                value=Name(lineno=1034, col_offset=39, id='overwrite_a', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=1035,
                    col_offset=4,
                    test=Compare(
                        lineno=1035,
                        col_offset=7,
                        left=Name(lineno=1035, col_offset=7, id='info', ctx=Load()),
                        ops=[Lt()],
                        comparators=[Num(lineno=1035, col_offset=14, n=0)],
                    ),
                    body=[
                        Raise(
                            lineno=1036,
                            col_offset=8,
                            exc=Call(
                                lineno=1036,
                                col_offset=14,
                                func=Name(lineno=1036, col_offset=14, id='ValueError', ctx=Load()),
                                args=[
                                    BinOp(
                                        lineno=1036,
                                        col_offset=25,
                                        left=Str(lineno=1036, col_offset=25, s='illegal value in %d-th argument of internal det.getrf'),
                                        op=Mod(),
                                        right=UnaryOp(
                                            lineno=1037,
                                            col_offset=39,
                                            op=USub(),
                                            operand=Name(lineno=1037, col_offset=40, id='info', ctx=Load()),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    lineno=1038,
                    col_offset=4,
                    value=Name(lineno=1038, col_offset=11, id='a_det', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=1042,
            col_offset=0,
            name='lstsq',
            args=arguments(
                args=[
                    arg(lineno=1042, col_offset=10, arg='a', annotation=None),
                    arg(lineno=1042, col_offset=13, arg='b', annotation=None),
                    arg(lineno=1042, col_offset=16, arg='cond', annotation=None),
                    arg(lineno=1042, col_offset=27, arg='overwrite_a', annotation=None),
                    arg(lineno=1042, col_offset=46, arg='overwrite_b', annotation=None),
                    arg(lineno=1043, col_offset=10, arg='check_finite', annotation=None),
                    arg(lineno=1043, col_offset=29, arg='lapack_driver', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    NameConstant(lineno=1042, col_offset=21, value=None),
                    NameConstant(lineno=1042, col_offset=39, value=False),
                    NameConstant(lineno=1042, col_offset=58, value=False),
                    NameConstant(lineno=1043, col_offset=23, value=True),
                    NameConstant(lineno=1043, col_offset=43, value=None),
                ],
            ),
            body=[
                Expr(
                    lineno=1151,
                    col_offset=-1,
                    value=Str(lineno=1151, col_offset=-1, s='\n    Compute least-squares solution to equation Ax = b.\n\n    Compute a vector x such that the 2-norm ``|b - A x|`` is minimized.\n\n    Parameters\n    ----------\n    a : (M, N) array_like\n        Left hand side array\n    b : (M,) or (M, K) array_like\n        Right hand side array\n    cond : float, optional\n        Cutoff for \'small\' singular values; used to determine effective\n        rank of a. Singular values smaller than\n        ``rcond * largest_singular_value`` are considered zero.\n    overwrite_a : bool, optional\n        Discard data in `a` (may enhance performance). Default is False.\n    overwrite_b : bool, optional\n        Discard data in `b` (may enhance performance). Default is False.\n    check_finite : bool, optional\n        Whether to check that the input matrices contain only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n    lapack_driver : str, optional\n        Which LAPACK driver is used to solve the least-squares problem.\n        Options are ``\'gelsd\'``, ``\'gelsy\'``, ``\'gelss\'``. Default\n        (``\'gelsd\'``) is a good choice.  However, ``\'gelsy\'`` can be slightly\n        faster on many problems.  ``\'gelss\'`` was used historically.  It is\n        generally slow but uses less memory.\n\n        .. versionadded:: 0.17.0\n\n    Returns\n    -------\n    x : (N,) or (N, K) ndarray\n        Least-squares solution.  Return shape matches shape of `b`.\n    residues : (K,) ndarray or float\n        Square of the 2-norm for each column in ``b - a x``, if ``M > N`` and\n        ``ndim(A) == n`` (returns a scalar if b is 1-D). Otherwise a\n        (0,)-shaped array is returned.\n    rank : int\n        Effective rank of `a`.\n    s : (min(M, N),) ndarray or None\n        Singular values of `a`. The condition number of a is\n        ``abs(s[0] / s[-1])``.\n\n    Raises\n    ------\n    LinAlgError\n        If computation does not converge.\n\n    ValueError\n        When parameters are not compatible.\n\n    See Also\n    --------\n    scipy.optimize.nnls : linear least squares with non-negativity constraint\n\n    Notes\n    -----\n    When ``\'gelsy\'`` is used as a driver, `residues` is set to a (0,)-shaped\n    array and `s` is always ``None``.\n\n    Examples\n    --------\n    >>> from scipy.linalg import lstsq\n    >>> import matplotlib.pyplot as plt\n\n    Suppose we have the following data:\n\n    >>> x = np.array([1, 2.5, 3.5, 4, 5, 7, 8.5])\n    >>> y = np.array([0.3, 1.1, 1.5, 2.0, 3.2, 6.6, 8.6])\n\n    We want to fit a quadratic polynomial of the form ``y = a + b*x**2``\n    to this data.  We first form the "design matrix" M, with a constant\n    column of 1s and a column containing ``x**2``:\n\n    >>> M = x[:, np.newaxis]**[0, 2]\n    >>> M\n    array([[  1.  ,   1.  ],\n           [  1.  ,   6.25],\n           [  1.  ,  12.25],\n           [  1.  ,  16.  ],\n           [  1.  ,  25.  ],\n           [  1.  ,  49.  ],\n           [  1.  ,  72.25]])\n\n    We want to find the least-squares solution to ``M.dot(p) = y``,\n    where ``p`` is a vector with length 2 that holds the parameters\n    ``a`` and ``b``.\n\n    >>> p, res, rnk, s = lstsq(M, y)\n    >>> p\n    array([ 0.20925829,  0.12013861])\n\n    Plot the data and the fitted curve.\n\n    >>> plt.plot(x, y, \'o\', label=\'data\')\n    >>> xx = np.linspace(0, 9, 101)\n    >>> yy = p[0] + p[1]*xx**2\n    >>> plt.plot(xx, yy, label=\'least squares fit, $y = a + bx^2$\')\n    >>> plt.xlabel(\'x\')\n    >>> plt.ylabel(\'y\')\n    >>> plt.legend(framealpha=1, shadow=True)\n    >>> plt.grid(alpha=0.25)\n    >>> plt.show()\n\n    '),
                ),
                Assign(
                    lineno=1152,
                    col_offset=4,
                    targets=[Name(lineno=1152, col_offset=4, id='a1', ctx=Store())],
                    value=Call(
                        lineno=1152,
                        col_offset=9,
                        func=Name(lineno=1152, col_offset=9, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=1152, col_offset=28, id='a', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=1152, col_offset=44, id='check_finite', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=1153,
                    col_offset=4,
                    targets=[Name(lineno=1153, col_offset=4, id='b1', ctx=Store())],
                    value=Call(
                        lineno=1153,
                        col_offset=9,
                        func=Name(lineno=1153, col_offset=9, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=1153, col_offset=28, id='b', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=1153, col_offset=44, id='check_finite', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=1154,
                    col_offset=4,
                    test=Compare(
                        lineno=1154,
                        col_offset=7,
                        left=Call(
                            lineno=1154,
                            col_offset=7,
                            func=Name(lineno=1154, col_offset=7, id='len', ctx=Load()),
                            args=[
                                Attribute(
                                    lineno=1154,
                                    col_offset=11,
                                    value=Name(lineno=1154, col_offset=11, id='a1', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                        ops=[NotEq()],
                        comparators=[Num(lineno=1154, col_offset=24, n=2)],
                    ),
                    body=[
                        Raise(
                            lineno=1155,
                            col_offset=8,
                            exc=Call(
                                lineno=1155,
                                col_offset=14,
                                func=Name(lineno=1155, col_offset=14, id='ValueError', ctx=Load()),
                                args=[Str(lineno=1155, col_offset=25, s='Input array a should be 2-D')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=1156,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=1156,
                            col_offset=4,
                            elts=[
                                Name(lineno=1156, col_offset=4, id='m', ctx=Store()),
                                Name(lineno=1156, col_offset=7, id='n', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Attribute(
                        lineno=1156,
                        col_offset=11,
                        value=Name(lineno=1156, col_offset=11, id='a1', ctx=Load()),
                        attr='shape',
                        ctx=Load(),
                    ),
                ),
                If(
                    lineno=1157,
                    col_offset=4,
                    test=Compare(
                        lineno=1157,
                        col_offset=7,
                        left=Call(
                            lineno=1157,
                            col_offset=7,
                            func=Name(lineno=1157, col_offset=7, id='len', ctx=Load()),
                            args=[
                                Attribute(
                                    lineno=1157,
                                    col_offset=11,
                                    value=Name(lineno=1157, col_offset=11, id='b1', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                        ops=[Eq()],
                        comparators=[Num(lineno=1157, col_offset=24, n=2)],
                    ),
                    body=[
                        Assign(
                            lineno=1158,
                            col_offset=8,
                            targets=[Name(lineno=1158, col_offset=8, id='nrhs', ctx=Store())],
                            value=Subscript(
                                lineno=1158,
                                col_offset=15,
                                value=Attribute(
                                    lineno=1158,
                                    col_offset=15,
                                    value=Name(lineno=1158, col_offset=15, id='b1', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                                slice=Index(
                                    value=Num(lineno=1158, col_offset=24, n=1),
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[
                        Assign(
                            lineno=1160,
                            col_offset=8,
                            targets=[Name(lineno=1160, col_offset=8, id='nrhs', ctx=Store())],
                            value=Num(lineno=1160, col_offset=15, n=1),
                        ),
                    ],
                ),
                If(
                    lineno=1161,
                    col_offset=4,
                    test=Compare(
                        lineno=1161,
                        col_offset=7,
                        left=Name(lineno=1161, col_offset=7, id='m', ctx=Load()),
                        ops=[NotEq()],
                        comparators=[
                            Subscript(
                                lineno=1161,
                                col_offset=12,
                                value=Attribute(
                                    lineno=1161,
                                    col_offset=12,
                                    value=Name(lineno=1161, col_offset=12, id='b1', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                                slice=Index(
                                    value=Num(lineno=1161, col_offset=21, n=0),
                                ),
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            lineno=1162,
                            col_offset=8,
                            exc=Call(
                                lineno=1162,
                                col_offset=14,
                                func=Name(lineno=1162, col_offset=14, id='ValueError', ctx=Load()),
                                args=[
                                    Call(
                                        lineno=1162,
                                        col_offset=25,
                                        func=Attribute(
                                            lineno=1162,
                                            col_offset=25,
                                            value=Str(lineno=1162, col_offset=25, s='Shape mismatch: a and b should have the same number of rows ({} != {}).'),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(lineno=1163, col_offset=55, id='m', ctx=Load()),
                                            Subscript(
                                                lineno=1163,
                                                col_offset=58,
                                                value=Attribute(
                                                    lineno=1163,
                                                    col_offset=58,
                                                    value=Name(lineno=1163, col_offset=58, id='b1', ctx=Load()),
                                                    attr='shape',
                                                    ctx=Load(),
                                                ),
                                                slice=Index(
                                                    value=Num(lineno=1163, col_offset=67, n=0),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=1164,
                    col_offset=4,
                    test=BoolOp(
                        lineno=1164,
                        col_offset=7,
                        op=Or(),
                        values=[
                            Compare(
                                lineno=1164,
                                col_offset=7,
                                left=Name(lineno=1164, col_offset=7, id='m', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Num(lineno=1164, col_offset=12, n=0)],
                            ),
                            Compare(
                                lineno=1164,
                                col_offset=17,
                                left=Name(lineno=1164, col_offset=17, id='n', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Num(lineno=1164, col_offset=22, n=0)],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            lineno=1165,
                            col_offset=8,
                            targets=[Name(lineno=1165, col_offset=8, id='x', ctx=Store())],
                            value=Call(
                                lineno=1165,
                                col_offset=12,
                                func=Attribute(
                                    lineno=1165,
                                    col_offset=12,
                                    value=Name(lineno=1165, col_offset=12, id='np', ctx=Load()),
                                    attr='zeros',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        lineno=1165,
                                        col_offset=21,
                                        left=Tuple(
                                            lineno=1165,
                                            col_offset=22,
                                            elts=[Name(lineno=1165, col_offset=22, id='n', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            lineno=1165,
                                            col_offset=28,
                                            value=Attribute(
                                                lineno=1165,
                                                col_offset=28,
                                                value=Name(lineno=1165, col_offset=28, id='b1', ctx=Load()),
                                                attr='shape',
                                                ctx=Load(),
                                            ),
                                            slice=Slice(
                                                lower=Num(lineno=1165, col_offset=37, n=1),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='dtype',
                                        value=Call(
                                            lineno=1165,
                                            col_offset=48,
                                            func=Attribute(
                                                lineno=1165,
                                                col_offset=48,
                                                value=Name(lineno=1165, col_offset=48, id='np', ctx=Load()),
                                                attr='common_type',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(lineno=1165, col_offset=63, id='a1', ctx=Load()),
                                                Name(lineno=1165, col_offset=67, id='b1', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        If(
                            lineno=1166,
                            col_offset=8,
                            test=Compare(
                                lineno=1166,
                                col_offset=11,
                                left=Name(lineno=1166, col_offset=11, id='n', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Num(lineno=1166, col_offset=16, n=0)],
                            ),
                            body=[
                                Assign(
                                    lineno=1167,
                                    col_offset=12,
                                    targets=[Name(lineno=1167, col_offset=12, id='residues', ctx=Store())],
                                    value=BinOp(
                                        lineno=1167,
                                        col_offset=23,
                                        left=Call(
                                            lineno=1167,
                                            col_offset=23,
                                            func=Attribute(
                                                lineno=1167,
                                                col_offset=23,
                                                value=Attribute(
                                                    lineno=1167,
                                                    col_offset=23,
                                                    value=Name(lineno=1167, col_offset=23, id='np', ctx=Load()),
                                                    attr='linalg',
                                                    ctx=Load(),
                                                ),
                                                attr='norm',
                                                ctx=Load(),
                                            ),
                                            args=[Name(lineno=1167, col_offset=38, id='b1', ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='axis',
                                                    value=Num(lineno=1167, col_offset=47, n=0),
                                                ),
                                            ],
                                        ),
                                        op=Pow(),
                                        right=Num(lineno=1167, col_offset=51, n=2),
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    lineno=1169,
                                    col_offset=12,
                                    targets=[Name(lineno=1169, col_offset=12, id='residues', ctx=Store())],
                                    value=Call(
                                        lineno=1169,
                                        col_offset=23,
                                        func=Attribute(
                                            lineno=1169,
                                            col_offset=23,
                                            value=Name(lineno=1169, col_offset=23, id='np', ctx=Load()),
                                            attr='empty',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                lineno=1169,
                                                col_offset=33,
                                                elts=[Num(lineno=1169, col_offset=33, n=0)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Return(
                            lineno=1170,
                            col_offset=8,
                            value=Tuple(
                                lineno=1170,
                                col_offset=15,
                                elts=[
                                    Name(lineno=1170, col_offset=15, id='x', ctx=Load()),
                                    Name(lineno=1170, col_offset=18, id='residues', ctx=Load()),
                                    Num(lineno=1170, col_offset=28, n=0),
                                    Call(
                                        lineno=1170,
                                        col_offset=31,
                                        func=Attribute(
                                            lineno=1170,
                                            col_offset=31,
                                            value=Name(lineno=1170, col_offset=31, id='np', ctx=Load()),
                                            attr='empty',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                lineno=1170,
                                                col_offset=41,
                                                elts=[Num(lineno=1170, col_offset=41, n=0)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=1172,
                    col_offset=4,
                    targets=[Name(lineno=1172, col_offset=4, id='driver', ctx=Store())],
                    value=Name(lineno=1172, col_offset=13, id='lapack_driver', ctx=Load()),
                ),
                If(
                    lineno=1173,
                    col_offset=4,
                    test=Compare(
                        lineno=1173,
                        col_offset=7,
                        left=Name(lineno=1173, col_offset=7, id='driver', ctx=Load()),
                        ops=[Is()],
                        comparators=[NameConstant(lineno=1173, col_offset=17, value=None)],
                    ),
                    body=[
                        Assign(
                            lineno=1174,
                            col_offset=8,
                            targets=[Name(lineno=1174, col_offset=8, id='driver', ctx=Store())],
                            value=Attribute(
                                lineno=1174,
                                col_offset=17,
                                value=Name(lineno=1174, col_offset=17, id='lstsq', ctx=Load()),
                                attr='default_lapack_driver',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=1175,
                    col_offset=4,
                    test=Compare(
                        lineno=1175,
                        col_offset=7,
                        left=Name(lineno=1175, col_offset=7, id='driver', ctx=Load()),
                        ops=[NotIn()],
                        comparators=[
                            Tuple(
                                lineno=1175,
                                col_offset=22,
                                elts=[
                                    Str(lineno=1175, col_offset=22, s='gelsd'),
                                    Str(lineno=1175, col_offset=31, s='gelsy'),
                                    Str(lineno=1175, col_offset=40, s='gelss'),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            lineno=1176,
                            col_offset=8,
                            exc=Call(
                                lineno=1176,
                                col_offset=14,
                                func=Name(lineno=1176, col_offset=14, id='ValueError', ctx=Load()),
                                args=[
                                    BinOp(
                                        lineno=1176,
                                        col_offset=25,
                                        left=Str(lineno=1176, col_offset=25, s='LAPACK driver "%s" is not found'),
                                        op=Mod(),
                                        right=Name(lineno=1176, col_offset=61, id='driver', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=1178,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=1178,
                            col_offset=4,
                            elts=[
                                Name(lineno=1178, col_offset=4, id='lapack_func', ctx=Store()),
                                Name(lineno=1178, col_offset=17, id='lapack_lwork', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        lineno=1178,
                        col_offset=32,
                        func=Name(lineno=1178, col_offset=32, id='get_lapack_funcs', ctx=Load()),
                        args=[
                            Tuple(
                                lineno=1178,
                                col_offset=50,
                                elts=[
                                    Name(lineno=1178, col_offset=50, id='driver', ctx=Load()),
                                    BinOp(
                                        lineno=1179,
                                        col_offset=49,
                                        left=Str(lineno=1179, col_offset=49, s='%s_lwork'),
                                        op=Mod(),
                                        right=Name(lineno=1179, col_offset=62, id='driver', ctx=Load()),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                lineno=1180,
                                col_offset=50,
                                elts=[
                                    Name(lineno=1180, col_offset=50, id='a1', ctx=Load()),
                                    Name(lineno=1180, col_offset=54, id='b1', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=1181,
                    col_offset=4,
                    targets=[Name(lineno=1181, col_offset=4, id='real_data', ctx=Store())],
                    value=IfExp(
                        lineno=1181,
                        col_offset=16,
                        test=Compare(
                            lineno=1181,
                            col_offset=25,
                            left=Attribute(
                                lineno=1181,
                                col_offset=25,
                                value=Attribute(
                                    lineno=1181,
                                    col_offset=25,
                                    value=Name(lineno=1181, col_offset=25, id='lapack_func', ctx=Load()),
                                    attr='dtype',
                                    ctx=Load(),
                                ),
                                attr='kind',
                                ctx=Load(),
                            ),
                            ops=[Eq()],
                            comparators=[Str(lineno=1181, col_offset=51, s='f')],
                        ),
                        body=NameConstant(lineno=1181, col_offset=16, value=True),
                        orelse=NameConstant(lineno=1181, col_offset=61, value=False),
                    ),
                ),
                If(
                    lineno=1183,
                    col_offset=4,
                    test=Compare(
                        lineno=1183,
                        col_offset=7,
                        left=Name(lineno=1183, col_offset=7, id='m', ctx=Load()),
                        ops=[Lt()],
                        comparators=[Name(lineno=1183, col_offset=11, id='n', ctx=Load())],
                    ),
                    body=[
                        If(
                            lineno=1186,
                            col_offset=8,
                            test=Compare(
                                lineno=1186,
                                col_offset=11,
                                left=Call(
                                    lineno=1186,
                                    col_offset=11,
                                    func=Name(lineno=1186, col_offset=11, id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            lineno=1186,
                                            col_offset=15,
                                            value=Name(lineno=1186, col_offset=15, id='b1', ctx=Load()),
                                            attr='shape',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Num(lineno=1186, col_offset=28, n=2)],
                            ),
                            body=[
                                Assign(
                                    lineno=1187,
                                    col_offset=12,
                                    targets=[Name(lineno=1187, col_offset=12, id='b2', ctx=Store())],
                                    value=Call(
                                        lineno=1187,
                                        col_offset=17,
                                        func=Attribute(
                                            lineno=1187,
                                            col_offset=17,
                                            value=Name(lineno=1187, col_offset=17, id='np', ctx=Load()),
                                            attr='zeros',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                lineno=1187,
                                                col_offset=27,
                                                elts=[
                                                    Name(lineno=1187, col_offset=27, id='n', ctx=Load()),
                                                    Name(lineno=1187, col_offset=30, id='nrhs', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='dtype',
                                                value=Attribute(
                                                    lineno=1187,
                                                    col_offset=43,
                                                    value=Name(lineno=1187, col_offset=43, id='lapack_func', ctx=Load()),
                                                    attr='dtype',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    lineno=1188,
                                    col_offset=12,
                                    targets=[
                                        Subscript(
                                            lineno=1188,
                                            col_offset=12,
                                            value=Name(lineno=1188, col_offset=12, id='b2', ctx=Load()),
                                            slice=ExtSlice(
                                                dims=[
                                                    Slice(
                                                        lower=None,
                                                        upper=Name(lineno=1188, col_offset=16, id='m', ctx=Load()),
                                                        step=None,
                                                    ),
                                                    Slice(lower=None, upper=None, step=None),
                                                ],
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(lineno=1188, col_offset=24, id='b1', ctx=Load()),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    lineno=1190,
                                    col_offset=12,
                                    targets=[Name(lineno=1190, col_offset=12, id='b2', ctx=Store())],
                                    value=Call(
                                        lineno=1190,
                                        col_offset=17,
                                        func=Attribute(
                                            lineno=1190,
                                            col_offset=17,
                                            value=Name(lineno=1190, col_offset=17, id='np', ctx=Load()),
                                            attr='zeros',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=1190, col_offset=26, id='n', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='dtype',
                                                value=Attribute(
                                                    lineno=1190,
                                                    col_offset=35,
                                                    value=Name(lineno=1190, col_offset=35, id='lapack_func', ctx=Load()),
                                                    attr='dtype',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    lineno=1191,
                                    col_offset=12,
                                    targets=[
                                        Subscript(
                                            lineno=1191,
                                            col_offset=12,
                                            value=Name(lineno=1191, col_offset=12, id='b2', ctx=Load()),
                                            slice=Slice(
                                                lower=None,
                                                upper=Name(lineno=1191, col_offset=16, id='m', ctx=Load()),
                                                step=None,
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(lineno=1191, col_offset=21, id='b1', ctx=Load()),
                                ),
                            ],
                        ),
                        Assign(
                            lineno=1192,
                            col_offset=8,
                            targets=[Name(lineno=1192, col_offset=8, id='b1', ctx=Store())],
                            value=Name(lineno=1192, col_offset=13, id='b2', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=1194,
                    col_offset=4,
                    targets=[Name(lineno=1194, col_offset=4, id='overwrite_a', ctx=Store())],
                    value=BoolOp(
                        lineno=1194,
                        col_offset=18,
                        op=Or(),
                        values=[
                            Name(lineno=1194, col_offset=18, id='overwrite_a', ctx=Load()),
                            Call(
                                lineno=1194,
                                col_offset=33,
                                func=Name(lineno=1194, col_offset=33, id='_datacopied', ctx=Load()),
                                args=[
                                    Name(lineno=1194, col_offset=45, id='a1', ctx=Load()),
                                    Name(lineno=1194, col_offset=49, id='a', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=1195,
                    col_offset=4,
                    targets=[Name(lineno=1195, col_offset=4, id='overwrite_b', ctx=Store())],
                    value=BoolOp(
                        lineno=1195,
                        col_offset=18,
                        op=Or(),
                        values=[
                            Name(lineno=1195, col_offset=18, id='overwrite_b', ctx=Load()),
                            Call(
                                lineno=1195,
                                col_offset=33,
                                func=Name(lineno=1195, col_offset=33, id='_datacopied', ctx=Load()),
                                args=[
                                    Name(lineno=1195, col_offset=45, id='b1', ctx=Load()),
                                    Name(lineno=1195, col_offset=49, id='b', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=1197,
                    col_offset=4,
                    test=Compare(
                        lineno=1197,
                        col_offset=7,
                        left=Name(lineno=1197, col_offset=7, id='cond', ctx=Load()),
                        ops=[Is()],
                        comparators=[NameConstant(lineno=1197, col_offset=15, value=None)],
                    ),
                    body=[
                        Assign(
                            lineno=1198,
                            col_offset=8,
                            targets=[Name(lineno=1198, col_offset=8, id='cond', ctx=Store())],
                            value=Attribute(
                                lineno=1198,
                                col_offset=15,
                                value=Call(
                                    lineno=1198,
                                    col_offset=15,
                                    func=Attribute(
                                        lineno=1198,
                                        col_offset=15,
                                        value=Name(lineno=1198, col_offset=15, id='np', ctx=Load()),
                                        attr='finfo',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            lineno=1198,
                                            col_offset=24,
                                            value=Name(lineno=1198, col_offset=24, id='lapack_func', ctx=Load()),
                                            attr='dtype',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='eps',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=1200,
                    col_offset=4,
                    test=Compare(
                        lineno=1200,
                        col_offset=7,
                        left=Name(lineno=1200, col_offset=7, id='driver', ctx=Load()),
                        ops=[In()],
                        comparators=[
                            Tuple(
                                lineno=1200,
                                col_offset=18,
                                elts=[
                                    Str(lineno=1200, col_offset=18, s='gelss'),
                                    Str(lineno=1200, col_offset=27, s='gelsd'),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        If(
                            lineno=1201,
                            col_offset=8,
                            test=Compare(
                                lineno=1201,
                                col_offset=11,
                                left=Name(lineno=1201, col_offset=11, id='driver', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Str(lineno=1201, col_offset=21, s='gelss')],
                            ),
                            body=[
                                Assign(
                                    lineno=1202,
                                    col_offset=12,
                                    targets=[Name(lineno=1202, col_offset=12, id='lwork', ctx=Store())],
                                    value=Call(
                                        lineno=1202,
                                        col_offset=20,
                                        func=Name(lineno=1202, col_offset=20, id='_compute_lwork', ctx=Load()),
                                        args=[
                                            Name(lineno=1202, col_offset=35, id='lapack_lwork', ctx=Load()),
                                            Name(lineno=1202, col_offset=49, id='m', ctx=Load()),
                                            Name(lineno=1202, col_offset=52, id='n', ctx=Load()),
                                            Name(lineno=1202, col_offset=55, id='nrhs', ctx=Load()),
                                            Name(lineno=1202, col_offset=61, id='cond', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    lineno=1203,
                                    col_offset=12,
                                    targets=[
                                        Tuple(
                                            lineno=1203,
                                            col_offset=12,
                                            elts=[
                                                Name(lineno=1203, col_offset=12, id='v', ctx=Store()),
                                                Name(lineno=1203, col_offset=15, id='x', ctx=Store()),
                                                Name(lineno=1203, col_offset=18, id='s', ctx=Store()),
                                                Name(lineno=1203, col_offset=21, id='rank', ctx=Store()),
                                                Name(lineno=1203, col_offset=27, id='work', ctx=Store()),
                                                Name(lineno=1203, col_offset=33, id='info', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=1203,
                                        col_offset=40,
                                        func=Name(lineno=1203, col_offset=40, id='lapack_func', ctx=Load()),
                                        args=[
                                            Name(lineno=1203, col_offset=52, id='a1', ctx=Load()),
                                            Name(lineno=1203, col_offset=56, id='b1', ctx=Load()),
                                            Name(lineno=1203, col_offset=60, id='cond', ctx=Load()),
                                            Name(lineno=1203, col_offset=66, id='lwork', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='overwrite_a',
                                                value=Name(lineno=1204, col_offset=64, id='overwrite_a', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='overwrite_b',
                                                value=Name(lineno=1205, col_offset=64, id='overwrite_b', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    lineno=1207,
                                    col_offset=13,
                                    test=Compare(
                                        lineno=1207,
                                        col_offset=13,
                                        left=Name(lineno=1207, col_offset=13, id='driver', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Str(lineno=1207, col_offset=23, s='gelsd')],
                                    ),
                                    body=[
                                        If(
                                            lineno=1208,
                                            col_offset=12,
                                            test=Name(lineno=1208, col_offset=15, id='real_data', ctx=Load()),
                                            body=[
                                                Assign(
                                                    lineno=1209,
                                                    col_offset=16,
                                                    targets=[
                                                        Tuple(
                                                            lineno=1209,
                                                            col_offset=16,
                                                            elts=[
                                                                Name(lineno=1209, col_offset=16, id='lwork', ctx=Store()),
                                                                Name(lineno=1209, col_offset=23, id='iwork', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        lineno=1209,
                                                        col_offset=31,
                                                        func=Name(lineno=1209, col_offset=31, id='_compute_lwork', ctx=Load()),
                                                        args=[
                                                            Name(lineno=1209, col_offset=46, id='lapack_lwork', ctx=Load()),
                                                            Name(lineno=1209, col_offset=60, id='m', ctx=Load()),
                                                            Name(lineno=1209, col_offset=63, id='n', ctx=Load()),
                                                            Name(lineno=1209, col_offset=66, id='nrhs', ctx=Load()),
                                                            Name(lineno=1209, col_offset=72, id='cond', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    lineno=1210,
                                                    col_offset=16,
                                                    targets=[
                                                        Tuple(
                                                            lineno=1210,
                                                            col_offset=16,
                                                            elts=[
                                                                Name(lineno=1210, col_offset=16, id='x', ctx=Store()),
                                                                Name(lineno=1210, col_offset=19, id='s', ctx=Store()),
                                                                Name(lineno=1210, col_offset=22, id='rank', ctx=Store()),
                                                                Name(lineno=1210, col_offset=28, id='info', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        lineno=1210,
                                                        col_offset=35,
                                                        func=Name(lineno=1210, col_offset=35, id='lapack_func', ctx=Load()),
                                                        args=[
                                                            Name(lineno=1210, col_offset=47, id='a1', ctx=Load()),
                                                            Name(lineno=1210, col_offset=51, id='b1', ctx=Load()),
                                                            Name(lineno=1210, col_offset=55, id='lwork', ctx=Load()),
                                                            Name(lineno=1211, col_offset=47, id='iwork', ctx=Load()),
                                                            Name(lineno=1211, col_offset=54, id='cond', ctx=Load()),
                                                            NameConstant(lineno=1211, col_offset=60, value=False),
                                                            NameConstant(lineno=1211, col_offset=67, value=False),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    lineno=1213,
                                                    col_offset=16,
                                                    targets=[
                                                        Tuple(
                                                            lineno=1213,
                                                            col_offset=16,
                                                            elts=[
                                                                Name(lineno=1213, col_offset=16, id='lwork', ctx=Store()),
                                                                Name(lineno=1213, col_offset=23, id='rwork', ctx=Store()),
                                                                Name(lineno=1213, col_offset=30, id='iwork', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        lineno=1213,
                                                        col_offset=38,
                                                        func=Name(lineno=1213, col_offset=38, id='_compute_lwork', ctx=Load()),
                                                        args=[
                                                            Name(lineno=1213, col_offset=53, id='lapack_lwork', ctx=Load()),
                                                            Name(lineno=1213, col_offset=67, id='m', ctx=Load()),
                                                            Name(lineno=1213, col_offset=70, id='n', ctx=Load()),
                                                            Name(lineno=1214, col_offset=53, id='nrhs', ctx=Load()),
                                                            Name(lineno=1214, col_offset=59, id='cond', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    lineno=1215,
                                                    col_offset=16,
                                                    targets=[
                                                        Tuple(
                                                            lineno=1215,
                                                            col_offset=16,
                                                            elts=[
                                                                Name(lineno=1215, col_offset=16, id='x', ctx=Store()),
                                                                Name(lineno=1215, col_offset=19, id='s', ctx=Store()),
                                                                Name(lineno=1215, col_offset=22, id='rank', ctx=Store()),
                                                                Name(lineno=1215, col_offset=28, id='info', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        lineno=1215,
                                                        col_offset=35,
                                                        func=Name(lineno=1215, col_offset=35, id='lapack_func', ctx=Load()),
                                                        args=[
                                                            Name(lineno=1215, col_offset=47, id='a1', ctx=Load()),
                                                            Name(lineno=1215, col_offset=51, id='b1', ctx=Load()),
                                                            Name(lineno=1215, col_offset=55, id='lwork', ctx=Load()),
                                                            Name(lineno=1215, col_offset=62, id='rwork', ctx=Load()),
                                                            Name(lineno=1215, col_offset=69, id='iwork', ctx=Load()),
                                                            Name(lineno=1216, col_offset=47, id='cond', ctx=Load()),
                                                            NameConstant(lineno=1216, col_offset=53, value=False),
                                                            NameConstant(lineno=1216, col_offset=60, value=False),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        If(
                            lineno=1217,
                            col_offset=8,
                            test=Compare(
                                lineno=1217,
                                col_offset=11,
                                left=Name(lineno=1217, col_offset=11, id='info', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Num(lineno=1217, col_offset=18, n=0)],
                            ),
                            body=[
                                Raise(
                                    lineno=1218,
                                    col_offset=12,
                                    exc=Call(
                                        lineno=1218,
                                        col_offset=18,
                                        func=Name(lineno=1218, col_offset=18, id='LinAlgError', ctx=Load()),
                                        args=[Str(lineno=1218, col_offset=30, s='SVD did not converge in Linear Least Squares')],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            lineno=1219,
                            col_offset=8,
                            test=Compare(
                                lineno=1219,
                                col_offset=11,
                                left=Name(lineno=1219, col_offset=11, id='info', ctx=Load()),
                                ops=[Lt()],
                                comparators=[Num(lineno=1219, col_offset=18, n=0)],
                            ),
                            body=[
                                Raise(
                                    lineno=1220,
                                    col_offset=12,
                                    exc=Call(
                                        lineno=1220,
                                        col_offset=18,
                                        func=Name(lineno=1220, col_offset=18, id='ValueError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                lineno=1220,
                                                col_offset=29,
                                                left=Str(lineno=1220, col_offset=29, s='illegal value in %d-th argument of internal %s'),
                                                op=Mod(),
                                                right=Tuple(
                                                    lineno=1221,
                                                    col_offset=32,
                                                    elts=[
                                                        UnaryOp(
                                                            lineno=1221,
                                                            col_offset=32,
                                                            op=USub(),
                                                            operand=Name(lineno=1221, col_offset=33, id='info', ctx=Load()),
                                                        ),
                                                        Name(lineno=1221, col_offset=39, id='lapack_driver', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            lineno=1222,
                            col_offset=8,
                            targets=[Name(lineno=1222, col_offset=8, id='resids', ctx=Store())],
                            value=Call(
                                lineno=1222,
                                col_offset=17,
                                func=Attribute(
                                    lineno=1222,
                                    col_offset=17,
                                    value=Name(lineno=1222, col_offset=17, id='np', ctx=Load()),
                                    attr='asarray',
                                    ctx=Load(),
                                ),
                                args=[List(lineno=1222, col_offset=28, elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='dtype',
                                        value=Attribute(
                                            lineno=1222,
                                            col_offset=38,
                                            value=Name(lineno=1222, col_offset=38, id='x', ctx=Load()),
                                            attr='dtype',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        If(
                            lineno=1223,
                            col_offset=8,
                            test=Compare(
                                lineno=1223,
                                col_offset=11,
                                left=Name(lineno=1223, col_offset=11, id='m', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Name(lineno=1223, col_offset=15, id='n', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    lineno=1224,
                                    col_offset=12,
                                    targets=[Name(lineno=1224, col_offset=12, id='x1', ctx=Store())],
                                    value=Subscript(
                                        lineno=1224,
                                        col_offset=17,
                                        value=Name(lineno=1224, col_offset=17, id='x', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Name(lineno=1224, col_offset=20, id='n', ctx=Load()),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                                If(
                                    lineno=1225,
                                    col_offset=12,
                                    test=Compare(
                                        lineno=1225,
                                        col_offset=15,
                                        left=Name(lineno=1225, col_offset=15, id='rank', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(lineno=1225, col_offset=23, id='n', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            lineno=1226,
                                            col_offset=16,
                                            targets=[Name(lineno=1226, col_offset=16, id='resids', ctx=Store())],
                                            value=Call(
                                                lineno=1226,
                                                col_offset=25,
                                                func=Attribute(
                                                    lineno=1226,
                                                    col_offset=25,
                                                    value=Name(lineno=1226, col_offset=25, id='np', ctx=Load()),
                                                    attr='sum',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        lineno=1226,
                                                        col_offset=32,
                                                        left=Call(
                                                            lineno=1226,
                                                            col_offset=32,
                                                            func=Attribute(
                                                                lineno=1226,
                                                                col_offset=32,
                                                                value=Name(lineno=1226, col_offset=32, id='np', ctx=Load()),
                                                                attr='abs',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Subscript(
                                                                    lineno=1226,
                                                                    col_offset=39,
                                                                    value=Name(lineno=1226, col_offset=39, id='x', ctx=Load()),
                                                                    slice=Slice(
                                                                        lower=Name(lineno=1226, col_offset=41, id='n', ctx=Load()),
                                                                        upper=None,
                                                                        step=None,
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        op=Pow(),
                                                        right=Num(lineno=1226, col_offset=47, n=2),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='axis',
                                                        value=Num(lineno=1226, col_offset=55, n=0),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    lineno=1227,
                                    col_offset=12,
                                    targets=[Name(lineno=1227, col_offset=12, id='x', ctx=Store())],
                                    value=Name(lineno=1227, col_offset=16, id='x1', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            lineno=1228,
                            col_offset=8,
                            value=Tuple(
                                lineno=1228,
                                col_offset=15,
                                elts=[
                                    Name(lineno=1228, col_offset=15, id='x', ctx=Load()),
                                    Name(lineno=1228, col_offset=18, id='resids', ctx=Load()),
                                    Name(lineno=1228, col_offset=26, id='rank', ctx=Load()),
                                    Name(lineno=1228, col_offset=32, id='s', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[
                        If(
                            lineno=1230,
                            col_offset=9,
                            test=Compare(
                                lineno=1230,
                                col_offset=9,
                                left=Name(lineno=1230, col_offset=9, id='driver', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Str(lineno=1230, col_offset=19, s='gelsy')],
                            ),
                            body=[
                                Assign(
                                    lineno=1231,
                                    col_offset=8,
                                    targets=[Name(lineno=1231, col_offset=8, id='lwork', ctx=Store())],
                                    value=Call(
                                        lineno=1231,
                                        col_offset=16,
                                        func=Name(lineno=1231, col_offset=16, id='_compute_lwork', ctx=Load()),
                                        args=[
                                            Name(lineno=1231, col_offset=31, id='lapack_lwork', ctx=Load()),
                                            Name(lineno=1231, col_offset=45, id='m', ctx=Load()),
                                            Name(lineno=1231, col_offset=48, id='n', ctx=Load()),
                                            Name(lineno=1231, col_offset=51, id='nrhs', ctx=Load()),
                                            Name(lineno=1231, col_offset=57, id='cond', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    lineno=1232,
                                    col_offset=8,
                                    targets=[Name(lineno=1232, col_offset=8, id='jptv', ctx=Store())],
                                    value=Call(
                                        lineno=1232,
                                        col_offset=15,
                                        func=Attribute(
                                            lineno=1232,
                                            col_offset=15,
                                            value=Name(lineno=1232, col_offset=15, id='np', ctx=Load()),
                                            attr='zeros',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                lineno=1232,
                                                col_offset=25,
                                                elts=[
                                                    Subscript(
                                                        lineno=1232,
                                                        col_offset=25,
                                                        value=Attribute(
                                                            lineno=1232,
                                                            col_offset=25,
                                                            value=Name(lineno=1232, col_offset=25, id='a1', ctx=Load()),
                                                            attr='shape',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Index(
                                                            value=Num(lineno=1232, col_offset=34, n=1),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    Num(lineno=1232, col_offset=38, n=1),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='dtype',
                                                value=Attribute(
                                                    lineno=1232,
                                                    col_offset=48,
                                                    value=Name(lineno=1232, col_offset=48, id='np', ctx=Load()),
                                                    attr='int32',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    lineno=1233,
                                    col_offset=8,
                                    targets=[
                                        Tuple(
                                            lineno=1233,
                                            col_offset=8,
                                            elts=[
                                                Name(lineno=1233, col_offset=8, id='v', ctx=Store()),
                                                Name(lineno=1233, col_offset=11, id='x', ctx=Store()),
                                                Name(lineno=1233, col_offset=14, id='j', ctx=Store()),
                                                Name(lineno=1233, col_offset=17, id='rank', ctx=Store()),
                                                Name(lineno=1233, col_offset=23, id='info', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        lineno=1233,
                                        col_offset=30,
                                        func=Name(lineno=1233, col_offset=30, id='lapack_func', ctx=Load()),
                                        args=[
                                            Name(lineno=1233, col_offset=42, id='a1', ctx=Load()),
                                            Name(lineno=1233, col_offset=46, id='b1', ctx=Load()),
                                            Name(lineno=1233, col_offset=50, id='jptv', ctx=Load()),
                                            Name(lineno=1233, col_offset=56, id='cond', ctx=Load()),
                                            Name(lineno=1234, col_offset=42, id='lwork', ctx=Load()),
                                            NameConstant(lineno=1234, col_offset=49, value=False),
                                            NameConstant(lineno=1234, col_offset=56, value=False),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    lineno=1235,
                                    col_offset=8,
                                    test=Compare(
                                        lineno=1235,
                                        col_offset=11,
                                        left=Name(lineno=1235, col_offset=11, id='info', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Num(lineno=1235, col_offset=18, n=0)],
                                    ),
                                    body=[
                                        Raise(
                                            lineno=1236,
                                            col_offset=12,
                                            exc=Call(
                                                lineno=1236,
                                                col_offset=18,
                                                func=Name(lineno=1236, col_offset=18, id='ValueError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        lineno=1236,
                                                        col_offset=29,
                                                        left=Str(lineno=1236, col_offset=29, s='illegal value in %d-th argument of internal gelsy'),
                                                        op=Mod(),
                                                        right=UnaryOp(
                                                            lineno=1237,
                                                            col_offset=39,
                                                            op=USub(),
                                                            operand=Name(lineno=1237, col_offset=40, id='info', ctx=Load()),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    lineno=1238,
                                    col_offset=8,
                                    test=Compare(
                                        lineno=1238,
                                        col_offset=11,
                                        left=Name(lineno=1238, col_offset=11, id='m', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Name(lineno=1238, col_offset=15, id='n', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            lineno=1239,
                                            col_offset=12,
                                            targets=[Name(lineno=1239, col_offset=12, id='x1', ctx=Store())],
                                            value=Subscript(
                                                lineno=1239,
                                                col_offset=17,
                                                value=Name(lineno=1239, col_offset=17, id='x', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Name(lineno=1239, col_offset=20, id='n', ctx=Load()),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                        ),
                                        Assign(
                                            lineno=1240,
                                            col_offset=12,
                                            targets=[Name(lineno=1240, col_offset=12, id='x', ctx=Store())],
                                            value=Name(lineno=1240, col_offset=16, id='x1', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    lineno=1241,
                                    col_offset=8,
                                    value=Tuple(
                                        lineno=1241,
                                        col_offset=15,
                                        elts=[
                                            Name(lineno=1241, col_offset=15, id='x', ctx=Load()),
                                            Call(
                                                lineno=1241,
                                                col_offset=18,
                                                func=Attribute(
                                                    lineno=1241,
                                                    col_offset=18,
                                                    value=Name(lineno=1241, col_offset=18, id='np', ctx=Load()),
                                                    attr='array',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(lineno=1241, col_offset=27, elts=[], ctx=Load()),
                                                    Attribute(
                                                        lineno=1241,
                                                        col_offset=31,
                                                        value=Name(lineno=1241, col_offset=31, id='x', ctx=Load()),
                                                        attr='dtype',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(lineno=1241, col_offset=41, id='rank', ctx=Load()),
                                            NameConstant(lineno=1241, col_offset=47, value=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        Assign(
            lineno=1244,
            col_offset=0,
            targets=[
                Attribute(
                    lineno=1244,
                    col_offset=0,
                    value=Name(lineno=1244, col_offset=0, id='lstsq', ctx=Load()),
                    attr='default_lapack_driver',
                    ctx=Store(),
                ),
            ],
            value=Str(lineno=1244, col_offset=30, s='gelsd'),
        ),
        FunctionDef(
            lineno=1247,
            col_offset=0,
            name='pinv',
            args=arguments(
                args=[
                    arg(lineno=1247, col_offset=9, arg='a', annotation=None),
                    arg(lineno=1247, col_offset=12, arg='cond', annotation=None),
                    arg(lineno=1247, col_offset=23, arg='rcond', annotation=None),
                    arg(lineno=1247, col_offset=35, arg='return_rank', annotation=None),
                    arg(lineno=1247, col_offset=54, arg='check_finite', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    NameConstant(lineno=1247, col_offset=17, value=None),
                    NameConstant(lineno=1247, col_offset=29, value=None),
                    NameConstant(lineno=1247, col_offset=47, value=False),
                    NameConstant(lineno=1247, col_offset=67, value=True),
                ],
            ),
            body=[
                Expr(
                    lineno=1293,
                    col_offset=-1,
                    value=Str(lineno=1293, col_offset=-1, s="\n    Compute the (Moore-Penrose) pseudo-inverse of a matrix.\n\n    Calculate a generalized inverse of a matrix using a least-squares\n    solver.\n\n    Parameters\n    ----------\n    a : (M, N) array_like\n        Matrix to be pseudo-inverted.\n    cond, rcond : float, optional\n        Cutoff for 'small' singular values in the least-squares solver.\n        Singular values smaller than ``rcond * largest_singular_value``\n        are considered zero.\n        If None, it is set to ``np.finfo(a.dtype).eps``.\n        If `a` is an array of integers, it is set to ``np.finfo('float64').eps``.\n    return_rank : bool, optional\n        if True, return the effective rank of the matrix\n    check_finite : bool, optional\n        Whether to check that the input matrix contains only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n\n    Returns\n    -------\n    B : (N, M) ndarray\n        The pseudo-inverse of matrix `a`.\n    rank : int\n        The effective rank of the matrix.  Returned if return_rank == True\n\n    Raises\n    ------\n    LinAlgError\n        If computation does not converge.\n\n    Examples\n    --------\n    >>> from scipy import linalg\n    >>> a = np.random.randn(9, 6)\n    >>> B = linalg.pinv(a)\n    >>> np.allclose(a, np.dot(a, np.dot(B, a)))\n    True\n    >>> np.allclose(B, np.dot(B, np.dot(a, B)))\n    True\n\n    "),
                ),
                Assign(
                    lineno=1294,
                    col_offset=4,
                    targets=[Name(lineno=1294, col_offset=4, id='a', ctx=Store())],
                    value=Call(
                        lineno=1294,
                        col_offset=8,
                        func=Name(lineno=1294, col_offset=8, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=1294, col_offset=27, id='a', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=1294, col_offset=43, id='check_finite', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=1295,
                    col_offset=4,
                    targets=[Name(lineno=1295, col_offset=4, id='b', ctx=Store())],
                    value=Call(
                        lineno=1295,
                        col_offset=8,
                        func=Attribute(
                            lineno=1295,
                            col_offset=8,
                            value=Name(lineno=1295, col_offset=8, id='np', ctx=Load()),
                            attr='identity',
                            ctx=Load(),
                        ),
                        args=[
                            Subscript(
                                lineno=1295,
                                col_offset=20,
                                value=Attribute(
                                    lineno=1295,
                                    col_offset=20,
                                    value=Name(lineno=1295, col_offset=20, id='a', ctx=Load()),
                                    attr='shape',
                                    ctx=Load(),
                                ),
                                slice=Index(
                                    value=Num(lineno=1295, col_offset=28, n=0),
                                ),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='dtype',
                                value=Attribute(
                                    lineno=1295,
                                    col_offset=38,
                                    value=Name(lineno=1295, col_offset=38, id='a', ctx=Load()),
                                    attr='dtype',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=1296,
                    col_offset=4,
                    test=Compare(
                        lineno=1296,
                        col_offset=7,
                        left=Name(lineno=1296, col_offset=7, id='rcond', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[NameConstant(lineno=1296, col_offset=20, value=None)],
                    ),
                    body=[
                        Assign(
                            lineno=1297,
                            col_offset=8,
                            targets=[Name(lineno=1297, col_offset=8, id='cond', ctx=Store())],
                            value=Name(lineno=1297, col_offset=15, id='rcond', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=1299,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=1299,
                            col_offset=4,
                            elts=[
                                Name(lineno=1299, col_offset=4, id='x', ctx=Store()),
                                Name(lineno=1299, col_offset=7, id='resids', ctx=Store()),
                                Name(lineno=1299, col_offset=15, id='rank', ctx=Store()),
                                Name(lineno=1299, col_offset=21, id='s', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        lineno=1299,
                        col_offset=25,
                        func=Name(lineno=1299, col_offset=25, id='lstsq', ctx=Load()),
                        args=[
                            Name(lineno=1299, col_offset=31, id='a', ctx=Load()),
                            Name(lineno=1299, col_offset=34, id='b', ctx=Load()),
                        ],
                        keywords=[
                            keyword(
                                arg='cond',
                                value=Name(lineno=1299, col_offset=42, id='cond', ctx=Load()),
                            ),
                            keyword(
                                arg='check_finite',
                                value=NameConstant(lineno=1299, col_offset=61, value=False),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=1301,
                    col_offset=4,
                    test=Name(lineno=1301, col_offset=7, id='return_rank', ctx=Load()),
                    body=[
                        Return(
                            lineno=1302,
                            col_offset=8,
                            value=Tuple(
                                lineno=1302,
                                col_offset=15,
                                elts=[
                                    Name(lineno=1302, col_offset=15, id='x', ctx=Load()),
                                    Name(lineno=1302, col_offset=18, id='rank', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[
                        Return(
                            lineno=1304,
                            col_offset=8,
                            value=Name(lineno=1304, col_offset=15, id='x', ctx=Load()),
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=1307,
            col_offset=0,
            name='pinv2',
            args=arguments(
                args=[
                    arg(lineno=1307, col_offset=10, arg='a', annotation=None),
                    arg(lineno=1307, col_offset=13, arg='cond', annotation=None),
                    arg(lineno=1307, col_offset=24, arg='rcond', annotation=None),
                    arg(lineno=1307, col_offset=36, arg='return_rank', annotation=None),
                    arg(lineno=1307, col_offset=55, arg='check_finite', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    NameConstant(lineno=1307, col_offset=18, value=None),
                    NameConstant(lineno=1307, col_offset=30, value=None),
                    NameConstant(lineno=1307, col_offset=48, value=False),
                    NameConstant(lineno=1307, col_offset=68, value=True),
                ],
            ),
            body=[
                Expr(
                    lineno=1355,
                    col_offset=-1,
                    value=Str(lineno=1355, col_offset=-1, s="\n    Compute the (Moore-Penrose) pseudo-inverse of a matrix.\n\n    Calculate a generalized inverse of a matrix using its\n    singular-value decomposition and including all 'large' singular\n    values.\n\n    Parameters\n    ----------\n    a : (M, N) array_like\n        Matrix to be pseudo-inverted.\n    cond, rcond : float or None\n        Cutoff for 'small' singular values.\n        Singular values smaller than ``rcond*largest_singular_value``\n        are considered zero.\n        If None and the dtype of `a` is ``np.float32``, it is set to\n        ``np.finfo('float32').eps * 1e3``.\n        Otherwise, it is set to ``np.finfo('float64').eps * 1e6``.\n    return_rank : bool, optional\n        If True, return the effective rank of the matrix.\n    check_finite : bool, optional\n        Whether to check that the input matrix contains only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n\n    Returns\n    -------\n    B : (N, M) ndarray\n        The pseudo-inverse of matrix `a`.\n    rank : int\n        The effective rank of the matrix.  Returned if `return_rank` is True.\n\n    Raises\n    ------\n    LinAlgError\n        If SVD computation does not converge.\n\n    Examples\n    --------\n    >>> from scipy import linalg\n    >>> a = np.random.randn(9, 6)\n    >>> B = linalg.pinv2(a)\n    >>> np.allclose(a, np.dot(a, np.dot(B, a)))\n    True\n    >>> np.allclose(B, np.dot(B, np.dot(a, B)))\n    True\n\n    "),
                ),
                Assign(
                    lineno=1356,
                    col_offset=4,
                    targets=[Name(lineno=1356, col_offset=4, id='a', ctx=Store())],
                    value=Call(
                        lineno=1356,
                        col_offset=8,
                        func=Name(lineno=1356, col_offset=8, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=1356, col_offset=27, id='a', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=1356, col_offset=43, id='check_finite', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=1357,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=1357,
                            col_offset=4,
                            elts=[
                                Name(lineno=1357, col_offset=4, id='u', ctx=Store()),
                                Name(lineno=1357, col_offset=7, id='s', ctx=Store()),
                                Name(lineno=1357, col_offset=10, id='vh', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        lineno=1357,
                        col_offset=15,
                        func=Attribute(
                            lineno=1357,
                            col_offset=15,
                            value=Name(lineno=1357, col_offset=15, id='decomp_svd', ctx=Load()),
                            attr='svd',
                            ctx=Load(),
                        ),
                        args=[Name(lineno=1357, col_offset=30, id='a', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='full_matrices',
                                value=NameConstant(lineno=1357, col_offset=47, value=False),
                            ),
                            keyword(
                                arg='check_finite',
                                value=NameConstant(lineno=1357, col_offset=67, value=False),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=1359,
                    col_offset=4,
                    test=Compare(
                        lineno=1359,
                        col_offset=7,
                        left=Name(lineno=1359, col_offset=7, id='rcond', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[NameConstant(lineno=1359, col_offset=20, value=None)],
                    ),
                    body=[
                        Assign(
                            lineno=1360,
                            col_offset=8,
                            targets=[Name(lineno=1360, col_offset=8, id='cond', ctx=Store())],
                            value=Name(lineno=1360, col_offset=15, id='rcond', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=1361,
                    col_offset=4,
                    test=Compare(
                        lineno=1361,
                        col_offset=7,
                        left=Name(lineno=1361, col_offset=7, id='cond', ctx=Load()),
                        ops=[In()],
                        comparators=[
                            List(
                                lineno=1361,
                                col_offset=15,
                                elts=[
                                    NameConstant(lineno=1361, col_offset=16, value=None),
                                    UnaryOp(
                                        lineno=1361,
                                        col_offset=22,
                                        op=USub(),
                                        operand=Num(lineno=1361, col_offset=23, n=1),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            lineno=1362,
                            col_offset=8,
                            targets=[Name(lineno=1362, col_offset=8, id='t', ctx=Store())],
                            value=Call(
                                lineno=1362,
                                col_offset=12,
                                func=Attribute(
                                    lineno=1362,
                                    col_offset=12,
                                    value=Attribute(
                                        lineno=1362,
                                        col_offset=12,
                                        value=Attribute(
                                            lineno=1362,
                                            col_offset=12,
                                            value=Name(lineno=1362, col_offset=12, id='u', ctx=Load()),
                                            attr='dtype',
                                            ctx=Load(),
                                        ),
                                        attr='char',
                                        ctx=Load(),
                                    ),
                                    attr='lower',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=1363,
                            col_offset=8,
                            targets=[Name(lineno=1363, col_offset=8, id='factor', ctx=Store())],
                            value=Dict(
                                lineno=1363,
                                col_offset=17,
                                keys=[
                                    Str(lineno=1363, col_offset=18, s='f'),
                                    Str(lineno=1363, col_offset=28, s='d'),
                                ],
                                values=[
                                    Num(lineno=1363, col_offset=23, n=1000.0),
                                    Num(lineno=1363, col_offset=33, n=1000000.0),
                                ],
                            ),
                        ),
                        Assign(
                            lineno=1364,
                            col_offset=8,
                            targets=[Name(lineno=1364, col_offset=8, id='cond', ctx=Store())],
                            value=BinOp(
                                lineno=1364,
                                col_offset=15,
                                left=Subscript(
                                    lineno=1364,
                                    col_offset=15,
                                    value=Name(lineno=1364, col_offset=15, id='factor', ctx=Load()),
                                    slice=Index(
                                        value=Name(lineno=1364, col_offset=22, id='t', ctx=Load()),
                                    ),
                                    ctx=Load(),
                                ),
                                op=Mult(),
                                right=Attribute(
                                    lineno=1364,
                                    col_offset=27,
                                    value=Call(
                                        lineno=1364,
                                        col_offset=27,
                                        func=Attribute(
                                            lineno=1364,
                                            col_offset=27,
                                            value=Name(lineno=1364, col_offset=27, id='np', ctx=Load()),
                                            attr='finfo',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=1364, col_offset=36, id='t', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='eps',
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=1366,
                    col_offset=4,
                    targets=[Name(lineno=1366, col_offset=4, id='rank', ctx=Store())],
                    value=Call(
                        lineno=1366,
                        col_offset=11,
                        func=Attribute(
                            lineno=1366,
                            col_offset=11,
                            value=Name(lineno=1366, col_offset=11, id='np', ctx=Load()),
                            attr='sum',
                            ctx=Load(),
                        ),
                        args=[
                            Compare(
                                lineno=1366,
                                col_offset=18,
                                left=Name(lineno=1366, col_offset=18, id='s', ctx=Load()),
                                ops=[Gt()],
                                comparators=[
                                    BinOp(
                                        lineno=1366,
                                        col_offset=22,
                                        left=Name(lineno=1366, col_offset=22, id='cond', ctx=Load()),
                                        op=Mult(),
                                        right=Call(
                                            lineno=1366,
                                            col_offset=29,
                                            func=Attribute(
                                                lineno=1366,
                                                col_offset=29,
                                                value=Name(lineno=1366, col_offset=29, id='np', ctx=Load()),
                                                attr='max',
                                                ctx=Load(),
                                            ),
                                            args=[Name(lineno=1366, col_offset=36, id='s', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=1368,
                    col_offset=4,
                    targets=[Name(lineno=1368, col_offset=4, id='u', ctx=Store())],
                    value=Subscript(
                        lineno=1368,
                        col_offset=8,
                        value=Name(lineno=1368, col_offset=8, id='u', ctx=Load()),
                        slice=ExtSlice(
                            dims=[
                                Slice(lower=None, upper=None, step=None),
                                Slice(
                                    lower=None,
                                    upper=Name(lineno=1368, col_offset=14, id='rank', ctx=Load()),
                                    step=None,
                                ),
                            ],
                        ),
                        ctx=Load(),
                    ),
                ),
                AugAssign(
                    lineno=1369,
                    col_offset=4,
                    target=Name(lineno=1369, col_offset=4, id='u', ctx=Store()),
                    op=Div(),
                    value=Subscript(
                        lineno=1369,
                        col_offset=9,
                        value=Name(lineno=1369, col_offset=9, id='s', ctx=Load()),
                        slice=Slice(
                            lower=None,
                            upper=Name(lineno=1369, col_offset=12, id='rank', ctx=Load()),
                            step=None,
                        ),
                        ctx=Load(),
                    ),
                ),
                Assign(
                    lineno=1370,
                    col_offset=4,
                    targets=[Name(lineno=1370, col_offset=4, id='B', ctx=Store())],
                    value=Call(
                        lineno=1370,
                        col_offset=8,
                        func=Attribute(
                            lineno=1370,
                            col_offset=8,
                            value=Name(lineno=1370, col_offset=8, id='np', ctx=Load()),
                            attr='transpose',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                lineno=1370,
                                col_offset=21,
                                func=Attribute(
                                    lineno=1370,
                                    col_offset=21,
                                    value=Name(lineno=1370, col_offset=21, id='np', ctx=Load()),
                                    attr='conjugate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        lineno=1370,
                                        col_offset=34,
                                        func=Attribute(
                                            lineno=1370,
                                            col_offset=34,
                                            value=Name(lineno=1370, col_offset=34, id='np', ctx=Load()),
                                            attr='dot',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(lineno=1370, col_offset=41, id='u', ctx=Load()),
                                            Subscript(
                                                lineno=1370,
                                                col_offset=44,
                                                value=Name(lineno=1370, col_offset=44, id='vh', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Name(lineno=1370, col_offset=48, id='rank', ctx=Load()),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=1372,
                    col_offset=4,
                    test=Name(lineno=1372, col_offset=7, id='return_rank', ctx=Load()),
                    body=[
                        Return(
                            lineno=1373,
                            col_offset=8,
                            value=Tuple(
                                lineno=1373,
                                col_offset=15,
                                elts=[
                                    Name(lineno=1373, col_offset=15, id='B', ctx=Load()),
                                    Name(lineno=1373, col_offset=18, id='rank', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[
                        Return(
                            lineno=1375,
                            col_offset=8,
                            value=Name(lineno=1375, col_offset=15, id='B', ctx=Load()),
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=1378,
            col_offset=0,
            name='pinvh',
            args=arguments(
                args=[
                    arg(lineno=1378, col_offset=10, arg='a', annotation=None),
                    arg(lineno=1378, col_offset=13, arg='cond', annotation=None),
                    arg(lineno=1378, col_offset=24, arg='rcond', annotation=None),
                    arg(lineno=1378, col_offset=36, arg='lower', annotation=None),
                    arg(lineno=1378, col_offset=48, arg='return_rank', annotation=None),
                    arg(lineno=1379, col_offset=10, arg='check_finite', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    NameConstant(lineno=1378, col_offset=18, value=None),
                    NameConstant(lineno=1378, col_offset=30, value=None),
                    NameConstant(lineno=1378, col_offset=42, value=True),
                    NameConstant(lineno=1378, col_offset=60, value=False),
                    NameConstant(lineno=1379, col_offset=23, value=True),
                ],
            ),
            body=[
                Expr(
                    lineno=1431,
                    col_offset=-1,
                    value=Str(lineno=1431, col_offset=-1, s="\n    Compute the (Moore-Penrose) pseudo-inverse of a Hermitian matrix.\n\n    Calculate a generalized inverse of a Hermitian or real symmetric matrix\n    using its eigenvalue decomposition and including all eigenvalues with\n    'large' absolute value.\n\n    Parameters\n    ----------\n    a : (N, N) array_like\n        Real symmetric or complex hermetian matrix to be pseudo-inverted\n    cond, rcond : float or None\n        Cutoff for 'small' singular values.\n        Singular values smaller than ``rcond*largest_singular_value``\n        are considered zero.\n        If None and the dtype of `a` is ``np.float32``, it is set to\n        ``np.finfo('float32').eps * 1e3``.\n        Otherwise, it is set to ``np.finfo('float64').eps * 1e6``.\n    lower : bool, optional\n        Whether the pertinent array data is taken from the lower or upper\n        triangle of `a`. (Default: lower)\n    return_rank : bool, optional\n        If True, return the effective rank of the matrix.\n    check_finite : bool, optional\n        Whether to check that the input matrix contains only finite numbers.\n        Disabling may give a performance gain, but may result in problems\n        (crashes, non-termination) if the inputs do contain infinities or NaNs.\n\n    Returns\n    -------\n    B : (N, N) ndarray\n        The pseudo-inverse of matrix `a`.\n    rank : int\n        The effective rank of the matrix.  Returned if `return_rank` is True.\n\n    Raises\n    ------\n    LinAlgError\n        If eigenvalue does not converge\n\n    Examples\n    --------\n    >>> from scipy.linalg import pinvh\n    >>> a = np.random.randn(9, 6)\n    >>> a = np.dot(a, a.T)\n    >>> B = pinvh(a)\n    >>> np.allclose(a, np.dot(a, np.dot(B, a)))\n    True\n    >>> np.allclose(B, np.dot(B, np.dot(a, B)))\n    True\n\n    "),
                ),
                Assign(
                    lineno=1432,
                    col_offset=4,
                    targets=[Name(lineno=1432, col_offset=4, id='a', ctx=Store())],
                    value=Call(
                        lineno=1432,
                        col_offset=8,
                        func=Name(lineno=1432, col_offset=8, id='_asarray_validated', ctx=Load()),
                        args=[Name(lineno=1432, col_offset=27, id='a', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='check_finite',
                                value=Name(lineno=1432, col_offset=43, id='check_finite', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=1433,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=1433,
                            col_offset=4,
                            elts=[
                                Name(lineno=1433, col_offset=4, id='s', ctx=Store()),
                                Name(lineno=1433, col_offset=7, id='u', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        lineno=1433,
                        col_offset=11,
                        func=Attribute(
                            lineno=1433,
                            col_offset=11,
                            value=Name(lineno=1433, col_offset=11, id='decomp', ctx=Load()),
                            attr='eigh',
                            ctx=Load(),
                        ),
                        args=[Name(lineno=1433, col_offset=23, id='a', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='lower',
                                value=Name(lineno=1433, col_offset=32, id='lower', ctx=Load()),
                            ),
                            keyword(
                                arg='check_finite',
                                value=NameConstant(lineno=1433, col_offset=52, value=False),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=1435,
                    col_offset=4,
                    test=Compare(
                        lineno=1435,
                        col_offset=7,
                        left=Name(lineno=1435, col_offset=7, id='rcond', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[NameConstant(lineno=1435, col_offset=20, value=None)],
                    ),
                    body=[
                        Assign(
                            lineno=1436,
                            col_offset=8,
                            targets=[Name(lineno=1436, col_offset=8, id='cond', ctx=Store())],
                            value=Name(lineno=1436, col_offset=15, id='rcond', ctx=Load()),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=1437,
                    col_offset=4,
                    test=Compare(
                        lineno=1437,
                        col_offset=7,
                        left=Name(lineno=1437, col_offset=7, id='cond', ctx=Load()),
                        ops=[In()],
                        comparators=[
                            List(
                                lineno=1437,
                                col_offset=15,
                                elts=[
                                    NameConstant(lineno=1437, col_offset=16, value=None),
                                    UnaryOp(
                                        lineno=1437,
                                        col_offset=22,
                                        op=USub(),
                                        operand=Num(lineno=1437, col_offset=23, n=1),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            lineno=1438,
                            col_offset=8,
                            targets=[Name(lineno=1438, col_offset=8, id='t', ctx=Store())],
                            value=Call(
                                lineno=1438,
                                col_offset=12,
                                func=Attribute(
                                    lineno=1438,
                                    col_offset=12,
                                    value=Attribute(
                                        lineno=1438,
                                        col_offset=12,
                                        value=Attribute(
                                            lineno=1438,
                                            col_offset=12,
                                            value=Name(lineno=1438, col_offset=12, id='u', ctx=Load()),
                                            attr='dtype',
                                            ctx=Load(),
                                        ),
                                        attr='char',
                                        ctx=Load(),
                                    ),
                                    attr='lower',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            lineno=1439,
                            col_offset=8,
                            targets=[Name(lineno=1439, col_offset=8, id='factor', ctx=Store())],
                            value=Dict(
                                lineno=1439,
                                col_offset=17,
                                keys=[
                                    Str(lineno=1439, col_offset=18, s='f'),
                                    Str(lineno=1439, col_offset=28, s='d'),
                                ],
                                values=[
                                    Num(lineno=1439, col_offset=23, n=1000.0),
                                    Num(lineno=1439, col_offset=33, n=1000000.0),
                                ],
                            ),
                        ),
                        Assign(
                            lineno=1440,
                            col_offset=8,
                            targets=[Name(lineno=1440, col_offset=8, id='cond', ctx=Store())],
                            value=BinOp(
                                lineno=1440,
                                col_offset=15,
                                left=Subscript(
                                    lineno=1440,
                                    col_offset=15,
                                    value=Name(lineno=1440, col_offset=15, id='factor', ctx=Load()),
                                    slice=Index(
                                        value=Name(lineno=1440, col_offset=22, id='t', ctx=Load()),
                                    ),
                                    ctx=Load(),
                                ),
                                op=Mult(),
                                right=Attribute(
                                    lineno=1440,
                                    col_offset=27,
                                    value=Call(
                                        lineno=1440,
                                        col_offset=27,
                                        func=Attribute(
                                            lineno=1440,
                                            col_offset=27,
                                            value=Name(lineno=1440, col_offset=27, id='np', ctx=Load()),
                                            attr='finfo',
                                            ctx=Load(),
                                        ),
                                        args=[Name(lineno=1440, col_offset=36, id='t', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='eps',
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=1443,
                    col_offset=4,
                    targets=[Name(lineno=1443, col_offset=4, id='above_cutoff', ctx=Store())],
                    value=Compare(
                        lineno=1443,
                        col_offset=20,
                        left=Call(
                            lineno=1443,
                            col_offset=20,
                            func=Name(lineno=1443, col_offset=20, id='abs', ctx=Load()),
                            args=[Name(lineno=1443, col_offset=24, id='s', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[Gt()],
                        comparators=[
                            BinOp(
                                lineno=1443,
                                col_offset=29,
                                left=Name(lineno=1443, col_offset=29, id='cond', ctx=Load()),
                                op=Mult(),
                                right=Call(
                                    lineno=1443,
                                    col_offset=36,
                                    func=Attribute(
                                        lineno=1443,
                                        col_offset=36,
                                        value=Name(lineno=1443, col_offset=36, id='np', ctx=Load()),
                                        attr='max',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            lineno=1443,
                                            col_offset=43,
                                            func=Name(lineno=1443, col_offset=43, id='abs', ctx=Load()),
                                            args=[Name(lineno=1443, col_offset=47, id='s', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=1444,
                    col_offset=4,
                    targets=[Name(lineno=1444, col_offset=4, id='psigma_diag', ctx=Store())],
                    value=BinOp(
                        lineno=1444,
                        col_offset=18,
                        left=Num(lineno=1444, col_offset=18, n=1.0),
                        op=Div(),
                        right=Subscript(
                            lineno=1444,
                            col_offset=24,
                            value=Name(lineno=1444, col_offset=24, id='s', ctx=Load()),
                            slice=Index(
                                value=Name(lineno=1444, col_offset=26, id='above_cutoff', ctx=Load()),
                            ),
                            ctx=Load(),
                        ),
                    ),
                ),
                Assign(
                    lineno=1445,
                    col_offset=4,
                    targets=[Name(lineno=1445, col_offset=4, id='u', ctx=Store())],
                    value=Subscript(
                        lineno=1445,
                        col_offset=8,
                        value=Name(lineno=1445, col_offset=8, id='u', ctx=Load()),
                        slice=ExtSlice(
                            dims=[
                                Slice(lower=None, upper=None, step=None),
                                Index(
                                    value=Name(lineno=1445, col_offset=13, id='above_cutoff', ctx=Load()),
                                ),
                            ],
                        ),
                        ctx=Load(),
                    ),
                ),
                Assign(
                    lineno=1447,
                    col_offset=4,
                    targets=[Name(lineno=1447, col_offset=4, id='B', ctx=Store())],
                    value=Call(
                        lineno=1447,
                        col_offset=8,
                        func=Attribute(
                            lineno=1447,
                            col_offset=8,
                            value=Name(lineno=1447, col_offset=8, id='np', ctx=Load()),
                            attr='dot',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                lineno=1447,
                                col_offset=15,
                                left=Name(lineno=1447, col_offset=15, id='u', ctx=Load()),
                                op=Mult(),
                                right=Name(lineno=1447, col_offset=19, id='psigma_diag', ctx=Load()),
                            ),
                            Attribute(
                                lineno=1447,
                                col_offset=32,
                                value=Call(
                                    lineno=1447,
                                    col_offset=32,
                                    func=Attribute(
                                        lineno=1447,
                                        col_offset=32,
                                        value=Name(lineno=1447, col_offset=32, id='np', ctx=Load()),
                                        attr='conjugate',
                                        ctx=Load(),
                                    ),
                                    args=[Name(lineno=1447, col_offset=45, id='u', ctx=Load())],
                                    keywords=[],
                                ),
                                attr='T',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=1449,
                    col_offset=4,
                    test=Name(lineno=1449, col_offset=7, id='return_rank', ctx=Load()),
                    body=[
                        Return(
                            lineno=1450,
                            col_offset=8,
                            value=Tuple(
                                lineno=1450,
                                col_offset=15,
                                elts=[
                                    Name(lineno=1450, col_offset=15, id='B', ctx=Load()),
                                    Call(
                                        lineno=1450,
                                        col_offset=18,
                                        func=Name(lineno=1450, col_offset=18, id='len', ctx=Load()),
                                        args=[Name(lineno=1450, col_offset=22, id='psigma_diag', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[
                        Return(
                            lineno=1452,
                            col_offset=8,
                            value=Name(lineno=1452, col_offset=15, id='B', ctx=Load()),
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
        FunctionDef(
            lineno=1455,
            col_offset=0,
            name='matrix_balance',
            args=arguments(
                args=[
                    arg(lineno=1455, col_offset=19, arg='A', annotation=None),
                    arg(lineno=1455, col_offset=22, arg='permute', annotation=None),
                    arg(lineno=1455, col_offset=36, arg='scale', annotation=None),
                    arg(lineno=1455, col_offset=48, arg='separate', annotation=None),
                    arg(lineno=1456, col_offset=19, arg='overwrite_a', annotation=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    NameConstant(lineno=1455, col_offset=30, value=True),
                    NameConstant(lineno=1455, col_offset=42, value=True),
                    NameConstant(lineno=1455, col_offset=57, value=False),
                    NameConstant(lineno=1456, col_offset=31, value=False),
                ],
            ),
            body=[
                Expr(
                    lineno=1555,
                    col_offset=-1,
                    value=Str(lineno=1555, col_offset=-1, s='\n    Compute a diagonal similarity transformation for row/column balancing.\n\n    The balancing tries to equalize the row and column 1-norms by applying\n    a similarity transformation such that the magnitude variation of the\n    matrix entries is reflected to the scaling matrices.\n\n    Moreover, if enabled, the matrix is first permuted to isolate the upper\n    triangular parts of the matrix and, again if scaling is also enabled,\n    only the remaining subblocks are subjected to scaling.\n\n    The balanced matrix satisfies the following equality\n\n    .. math::\n\n                        B = T^{-1} A T\n\n    The scaling coefficients are approximated to the nearest power of 2\n    to avoid round-off errors.\n\n    Parameters\n    ----------\n    A : (n, n) array_like\n        Square data matrix for the balancing.\n    permute : bool, optional\n        The selector to define whether permutation of A is also performed\n        prior to scaling.\n    scale : bool, optional\n        The selector to turn on and off the scaling. If False, the matrix\n        will not be scaled.\n    separate : bool, optional\n        This switches from returning a full matrix of the transformation\n        to a tuple of two separate 1D permutation and scaling arrays.\n    overwrite_a : bool, optional\n        This is passed to xGEBAL directly. Essentially, overwrites the result\n        to the data. It might increase the space efficiency. See LAPACK manual\n        for details. This is False by default.\n\n    Returns\n    -------\n    B : (n, n) ndarray\n        Balanced matrix\n    T : (n, n) ndarray\n        A possibly permuted diagonal matrix whose nonzero entries are\n        integer powers of 2 to avoid numerical truncation errors.\n    scale, perm : (n,) ndarray\n        If ``separate`` keyword is set to True then instead of the array\n        ``T`` above, the scaling and the permutation vectors are given\n        separately as a tuple without allocating the full array ``T``.\n\n    Notes\n    -----\n\n    This algorithm is particularly useful for eigenvalue and matrix\n    decompositions and in many cases it is already called by various\n    LAPACK routines.\n\n    The algorithm is based on the well-known technique of [1]_ and has\n    been modified to account for special cases. See [2]_ for details\n    which have been implemented since LAPACK v3.5.0. Before this version\n    there are corner cases where balancing can actually worsen the\n    conditioning. See [3]_ for such examples.\n\n    The code is a wrapper around LAPACK\'s xGEBAL routine family for matrix\n    balancing.\n\n    .. versionadded:: 0.19.0\n\n    Examples\n    --------\n    >>> from scipy import linalg\n    >>> x = np.array([[1,2,0], [9,1,0.01], [1,2,10*np.pi]])\n\n    >>> y, permscale = linalg.matrix_balance(x)\n    >>> np.abs(x).sum(axis=0) / np.abs(x).sum(axis=1)\n    array([ 3.66666667,  0.4995005 ,  0.91312162])\n\n    >>> np.abs(y).sum(axis=0) / np.abs(y).sum(axis=1)\n    array([ 1.2       ,  1.27041742,  0.92658316])  # may vary\n\n    >>> permscale  # only powers of 2 (0.5 == 2^(-1))\n    array([[  0.5,   0. ,  0. ],  # may vary\n           [  0. ,   1. ,  0. ],\n           [  0. ,   0. ,  1. ]])\n\n    References\n    ----------\n    .. [1] : B.N. Parlett and C. Reinsch, "Balancing a Matrix for\n       Calculation of Eigenvalues and Eigenvectors", Numerische Mathematik,\n       Vol.13(4), 1969, DOI:10.1007/BF02165404\n\n    .. [2] : R. James, J. Langou, B.R. Lowery, "On matrix balancing and\n       eigenvector computation", 2014, Available online:\n       https://arxiv.org/abs/1401.5766\n\n    .. [3] :  D.S. Watkins. A case where balancing is harmful.\n       Electron. Trans. Numer. Anal, Vol.23, 2006.\n\n    '),
                ),
                Assign(
                    lineno=1557,
                    col_offset=4,
                    targets=[Name(lineno=1557, col_offset=4, id='A', ctx=Store())],
                    value=Call(
                        lineno=1557,
                        col_offset=8,
                        func=Attribute(
                            lineno=1557,
                            col_offset=8,
                            value=Name(lineno=1557, col_offset=8, id='np', ctx=Load()),
                            attr='atleast_2d',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                lineno=1557,
                                col_offset=22,
                                func=Name(lineno=1557, col_offset=22, id='_asarray_validated', ctx=Load()),
                                args=[Name(lineno=1557, col_offset=41, id='A', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='check_finite',
                                        value=NameConstant(lineno=1557, col_offset=57, value=True),
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=1559,
                    col_offset=4,
                    test=UnaryOp(
                        lineno=1559,
                        col_offset=7,
                        op=Not(),
                        operand=Call(
                            lineno=1559,
                            col_offset=11,
                            func=Attribute(
                                lineno=1559,
                                col_offset=11,
                                value=Name(lineno=1559, col_offset=11, id='np', ctx=Load()),
                                attr='equal',
                                ctx=Load(),
                            ),
                            args=[
                                Starred(
                                    lineno=1559,
                                    col_offset=20,
                                    value=Attribute(
                                        lineno=1559,
                                        col_offset=21,
                                        value=Name(lineno=1559, col_offset=21, id='A', ctx=Load()),
                                        attr='shape',
                                        ctx=Load(),
                                    ),
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Raise(
                            lineno=1560,
                            col_offset=8,
                            exc=Call(
                                lineno=1560,
                                col_offset=14,
                                func=Name(lineno=1560, col_offset=14, id='ValueError', ctx=Load()),
                                args=[Str(lineno=1560, col_offset=25, s='The data matrix for balancing should be square.')],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=1562,
                    col_offset=4,
                    targets=[Name(lineno=1562, col_offset=4, id='gebal', ctx=Store())],
                    value=Call(
                        lineno=1562,
                        col_offset=12,
                        func=Name(lineno=1562, col_offset=12, id='get_lapack_funcs', ctx=Load()),
                        args=[
                            Str(lineno=1562, col_offset=30, s='gebal'),
                            Tuple(
                                lineno=1562,
                                col_offset=41,
                                elts=[Name(lineno=1562, col_offset=41, id='A', ctx=Load())],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=1563,
                    col_offset=4,
                    targets=[
                        Tuple(
                            lineno=1563,
                            col_offset=4,
                            elts=[
                                Name(lineno=1563, col_offset=4, id='B', ctx=Store()),
                                Name(lineno=1563, col_offset=7, id='lo', ctx=Store()),
                                Name(lineno=1563, col_offset=11, id='hi', ctx=Store()),
                                Name(lineno=1563, col_offset=15, id='ps', ctx=Store()),
                                Name(lineno=1563, col_offset=19, id='info', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        lineno=1563,
                        col_offset=26,
                        func=Name(lineno=1563, col_offset=26, id='gebal', ctx=Load()),
                        args=[Name(lineno=1563, col_offset=32, id='A', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='scale',
                                value=Name(lineno=1563, col_offset=41, id='scale', ctx=Load()),
                            ),
                            keyword(
                                arg='permute',
                                value=Name(lineno=1563, col_offset=56, id='permute', ctx=Load()),
                            ),
                            keyword(
                                arg='overwrite_a',
                                value=Name(lineno=1564, col_offset=44, id='overwrite_a', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                If(
                    lineno=1566,
                    col_offset=4,
                    test=Compare(
                        lineno=1566,
                        col_offset=7,
                        left=Name(lineno=1566, col_offset=7, id='info', ctx=Load()),
                        ops=[Lt()],
                        comparators=[Num(lineno=1566, col_offset=14, n=0)],
                    ),
                    body=[
                        Raise(
                            lineno=1567,
                            col_offset=8,
                            exc=Call(
                                lineno=1567,
                                col_offset=14,
                                func=Name(lineno=1567, col_offset=14, id='ValueError', ctx=Load()),
                                args=[
                                    Call(
                                        lineno=1567,
                                        col_offset=25,
                                        func=Attribute(
                                            lineno=1567,
                                            col_offset=25,
                                            value=Str(lineno=1567, col_offset=25, s='xGEBAL exited with the internal error "illegal value in argument number {}.". See LAPACK documentation for the xGEBAL error codes.'),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            UnaryOp(
                                                lineno=1570,
                                                col_offset=35,
                                                op=USub(),
                                                operand=Name(lineno=1570, col_offset=36, id='info', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=1573,
                    col_offset=4,
                    targets=[Name(lineno=1573, col_offset=4, id='scaling', ctx=Store())],
                    value=Call(
                        lineno=1573,
                        col_offset=14,
                        func=Attribute(
                            lineno=1573,
                            col_offset=14,
                            value=Name(lineno=1573, col_offset=14, id='np', ctx=Load()),
                            attr='ones_like',
                            ctx=Load(),
                        ),
                        args=[Name(lineno=1573, col_offset=27, id='ps', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='dtype',
                                value=Name(lineno=1573, col_offset=37, id='float', ctx=Load()),
                            ),
                        ],
                    ),
                ),
                Assign(
                    lineno=1574,
                    col_offset=4,
                    targets=[
                        Subscript(
                            lineno=1574,
                            col_offset=4,
                            value=Name(lineno=1574, col_offset=4, id='scaling', ctx=Load()),
                            slice=Slice(
                                lower=Name(lineno=1574, col_offset=12, id='lo', ctx=Load()),
                                upper=BinOp(
                                    lineno=1574,
                                    col_offset=15,
                                    left=Name(lineno=1574, col_offset=15, id='hi', ctx=Load()),
                                    op=Add(),
                                    right=Num(lineno=1574, col_offset=18, n=1),
                                ),
                                step=None,
                            ),
                            ctx=Store(),
                        ),
                    ],
                    value=Subscript(
                        lineno=1574,
                        col_offset=23,
                        value=Name(lineno=1574, col_offset=23, id='ps', ctx=Load()),
                        slice=Slice(
                            lower=Name(lineno=1574, col_offset=26, id='lo', ctx=Load()),
                            upper=BinOp(
                                lineno=1574,
                                col_offset=29,
                                left=Name(lineno=1574, col_offset=29, id='hi', ctx=Load()),
                                op=Add(),
                                right=Num(lineno=1574, col_offset=32, n=1),
                            ),
                            step=None,
                        ),
                        ctx=Load(),
                    ),
                ),
                Assign(
                    lineno=1577,
                    col_offset=4,
                    targets=[Name(lineno=1577, col_offset=4, id='ps', ctx=Store())],
                    value=BinOp(
                        lineno=1577,
                        col_offset=9,
                        left=Call(
                            lineno=1577,
                            col_offset=9,
                            func=Attribute(
                                lineno=1577,
                                col_offset=9,
                                value=Name(lineno=1577, col_offset=9, id='ps', ctx=Load()),
                                attr='astype',
                                ctx=Load(),
                            ),
                            args=[Name(lineno=1577, col_offset=19, id='int', ctx=Load())],
                            keywords=[
                                keyword(
                                    arg='copy',
                                    value=NameConstant(lineno=1577, col_offset=29, value=False),
                                ),
                            ],
                        ),
                        op=Sub(),
                        right=Num(lineno=1577, col_offset=38, n=1),
                    ),
                ),
                Assign(
                    lineno=1578,
                    col_offset=4,
                    targets=[Name(lineno=1578, col_offset=4, id='n', ctx=Store())],
                    value=Subscript(
                        lineno=1578,
                        col_offset=8,
                        value=Attribute(
                            lineno=1578,
                            col_offset=8,
                            value=Name(lineno=1578, col_offset=8, id='A', ctx=Load()),
                            attr='shape',
                            ctx=Load(),
                        ),
                        slice=Index(
                            value=Num(lineno=1578, col_offset=16, n=0),
                        ),
                        ctx=Load(),
                    ),
                ),
                Assign(
                    lineno=1579,
                    col_offset=4,
                    targets=[Name(lineno=1579, col_offset=4, id='perm', ctx=Store())],
                    value=Call(
                        lineno=1579,
                        col_offset=11,
                        func=Attribute(
                            lineno=1579,
                            col_offset=11,
                            value=Name(lineno=1579, col_offset=11, id='np', ctx=Load()),
                            attr='arange',
                            ctx=Load(),
                        ),
                        args=[Name(lineno=1579, col_offset=21, id='n', ctx=Load())],
                        keywords=[],
                    ),
                ),
                If(
                    lineno=1582,
                    col_offset=4,
                    test=Compare(
                        lineno=1582,
                        col_offset=7,
                        left=Name(lineno=1582, col_offset=7, id='hi', ctx=Load()),
                        ops=[Lt()],
                        comparators=[Name(lineno=1582, col_offset=12, id='n', ctx=Load())],
                    ),
                    body=[
                        For(
                            lineno=1583,
                            col_offset=8,
                            target=Tuple(
                                lineno=1583,
                                col_offset=12,
                                elts=[
                                    Name(lineno=1583, col_offset=12, id='ind', ctx=Store()),
                                    Name(lineno=1583, col_offset=17, id='x', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                lineno=1583,
                                col_offset=22,
                                func=Name(lineno=1583, col_offset=22, id='enumerate', ctx=Load()),
                                args=[
                                    Subscript(
                                        lineno=1583,
                                        col_offset=32,
                                        value=Subscript(
                                            lineno=1583,
                                            col_offset=32,
                                            value=Name(lineno=1583, col_offset=32, id='ps', ctx=Load()),
                                            slice=Slice(
                                                lower=BinOp(
                                                    lineno=1583,
                                                    col_offset=35,
                                                    left=Name(lineno=1583, col_offset=35, id='hi', ctx=Load()),
                                                    op=Add(),
                                                    right=Num(lineno=1583, col_offset=38, n=1),
                                                ),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=None,
                                            step=UnaryOp(
                                                lineno=1583,
                                                col_offset=44,
                                                op=USub(),
                                                operand=Num(lineno=1583, col_offset=45, n=1),
                                            ),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Num(lineno=1583, col_offset=49, n=1),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    lineno=1584,
                                    col_offset=12,
                                    test=Compare(
                                        lineno=1584,
                                        col_offset=15,
                                        left=BinOp(
                                            lineno=1584,
                                            col_offset=15,
                                            left=Name(lineno=1584, col_offset=15, id='n', ctx=Load()),
                                            op=Sub(),
                                            right=Name(lineno=1584, col_offset=17, id='ind', ctx=Load()),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(lineno=1584, col_offset=24, id='x', ctx=Load())],
                                    ),
                                    body=[Continue(lineno=1585, col_offset=16)],
                                    orelse=[],
                                ),
                                Assign(
                                    lineno=1586,
                                    col_offset=12,
                                    targets=[
                                        Subscript(
                                            lineno=1586,
                                            col_offset=12,
                                            value=Name(lineno=1586, col_offset=12, id='perm', ctx=Load()),
                                            slice=Index(
                                                value=List(
                                                    lineno=1586,
                                                    col_offset=17,
                                                    elts=[
                                                        Name(lineno=1586, col_offset=18, id='x', ctx=Load()),
                                                        BinOp(
                                                            lineno=1586,
                                                            col_offset=21,
                                                            left=Name(lineno=1586, col_offset=21, id='n', ctx=Load()),
                                                            op=Sub(),
                                                            right=Name(lineno=1586, col_offset=23, id='ind', ctx=Load()),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        lineno=1586,
                                        col_offset=31,
                                        value=Name(lineno=1586, col_offset=31, id='perm', ctx=Load()),
                                        slice=Index(
                                            value=List(
                                                lineno=1586,
                                                col_offset=36,
                                                elts=[
                                                    BinOp(
                                                        lineno=1586,
                                                        col_offset=37,
                                                        left=Name(lineno=1586, col_offset=37, id='n', ctx=Load()),
                                                        op=Sub(),
                                                        right=Name(lineno=1586, col_offset=39, id='ind', ctx=Load()),
                                                    ),
                                                    Name(lineno=1586, col_offset=44, id='x', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=1588,
                    col_offset=4,
                    test=Compare(
                        lineno=1588,
                        col_offset=7,
                        left=Name(lineno=1588, col_offset=7, id='lo', ctx=Load()),
                        ops=[Gt()],
                        comparators=[Num(lineno=1588, col_offset=12, n=0)],
                    ),
                    body=[
                        For(
                            lineno=1589,
                            col_offset=8,
                            target=Tuple(
                                lineno=1589,
                                col_offset=12,
                                elts=[
                                    Name(lineno=1589, col_offset=12, id='ind', ctx=Store()),
                                    Name(lineno=1589, col_offset=17, id='x', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                lineno=1589,
                                col_offset=22,
                                func=Name(lineno=1589, col_offset=22, id='enumerate', ctx=Load()),
                                args=[
                                    Subscript(
                                        lineno=1589,
                                        col_offset=32,
                                        value=Name(lineno=1589, col_offset=32, id='ps', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Name(lineno=1589, col_offset=36, id='lo', ctx=Load()),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    lineno=1590,
                                    col_offset=12,
                                    test=Compare(
                                        lineno=1590,
                                        col_offset=15,
                                        left=Name(lineno=1590, col_offset=15, id='ind', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(lineno=1590, col_offset=22, id='x', ctx=Load())],
                                    ),
                                    body=[Continue(lineno=1591, col_offset=16)],
                                    orelse=[],
                                ),
                                Assign(
                                    lineno=1592,
                                    col_offset=12,
                                    targets=[
                                        Subscript(
                                            lineno=1592,
                                            col_offset=12,
                                            value=Name(lineno=1592, col_offset=12, id='perm', ctx=Load()),
                                            slice=Index(
                                                value=List(
                                                    lineno=1592,
                                                    col_offset=17,
                                                    elts=[
                                                        Name(lineno=1592, col_offset=18, id='x', ctx=Load()),
                                                        Name(lineno=1592, col_offset=21, id='ind', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        lineno=1592,
                                        col_offset=29,
                                        value=Name(lineno=1592, col_offset=29, id='perm', ctx=Load()),
                                        slice=Index(
                                            value=List(
                                                lineno=1592,
                                                col_offset=34,
                                                elts=[
                                                    Name(lineno=1592, col_offset=35, id='ind', ctx=Load()),
                                                    Name(lineno=1592, col_offset=40, id='x', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    lineno=1594,
                    col_offset=4,
                    test=Name(lineno=1594, col_offset=7, id='separate', ctx=Load()),
                    body=[
                        Return(
                            lineno=1595,
                            col_offset=8,
                            value=Tuple(
                                lineno=1595,
                                col_offset=15,
                                elts=[
                                    Name(lineno=1595, col_offset=15, id='B', ctx=Load()),
                                    Tuple(
                                        lineno=1595,
                                        col_offset=19,
                                        elts=[
                                            Name(lineno=1595, col_offset=19, id='scaling', ctx=Load()),
                                            Name(lineno=1595, col_offset=28, id='perm', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    lineno=1598,
                    col_offset=4,
                    targets=[Name(lineno=1598, col_offset=4, id='iperm', ctx=Store())],
                    value=Call(
                        lineno=1598,
                        col_offset=12,
                        func=Attribute(
                            lineno=1598,
                            col_offset=12,
                            value=Name(lineno=1598, col_offset=12, id='np', ctx=Load()),
                            attr='empty_like',
                            ctx=Load(),
                        ),
                        args=[Name(lineno=1598, col_offset=26, id='perm', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Assign(
                    lineno=1599,
                    col_offset=4,
                    targets=[
                        Subscript(
                            lineno=1599,
                            col_offset=4,
                            value=Name(lineno=1599, col_offset=4, id='iperm', ctx=Load()),
                            slice=Index(
                                value=Name(lineno=1599, col_offset=10, id='perm', ctx=Load()),
                            ),
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        lineno=1599,
                        col_offset=18,
                        func=Attribute(
                            lineno=1599,
                            col_offset=18,
                            value=Name(lineno=1599, col_offset=18, id='np', ctx=Load()),
                            attr='arange',
                            ctx=Load(),
                        ),
                        args=[Name(lineno=1599, col_offset=28, id='n', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Return(
                    lineno=1601,
                    col_offset=4,
                    value=Tuple(
                        lineno=1601,
                        col_offset=11,
                        elts=[
                            Name(lineno=1601, col_offset=11, id='B', ctx=Load()),
                            Subscript(
                                lineno=1601,
                                col_offset=14,
                                value=Call(
                                    lineno=1601,
                                    col_offset=14,
                                    func=Attribute(
                                        lineno=1601,
                                        col_offset=14,
                                        value=Name(lineno=1601, col_offset=14, id='np', ctx=Load()),
                                        attr='diag',
                                        ctx=Load(),
                                    ),
                                    args=[Name(lineno=1601, col_offset=22, id='scaling', ctx=Load())],
                                    keywords=[],
                                ),
                                slice=ExtSlice(
                                    dims=[
                                        Index(
                                            value=Name(lineno=1601, col_offset=31, id='iperm', ctx=Load()),
                                        ),
                                        Slice(lower=None, upper=None, step=None),
                                    ],
                                ),
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
        ),
    ],
)