import os
import numpy as np
import pandas as pd
import tsfel

POLLUTANS = ["CO", "NO2", "SO2", "CH4"]

domain_list = ["statistical", "temporal", "spectral"]

FITUR_TARGET = [
    "f1_abs_energy","f2_auc","f3_autocorr","f4_average_power","f5_calc_centroid",
    "f6_calc_max","f7_calc_mean","f8_calc_median","f9_calc_min","f10_calc_std",
    "f11_calc_var","f12_dfa","f13_distance","f14_ecdf","f15_ecdf_percentile",
    "f16_ecdf_percentile_count","f17_ecdf_slope","f18_entropy","f19_fundamental_frequency",
    "f20_higuchi_fractal_dimension","f21_hist_mode","f22_human_range_energy","f23_hurst_exponent",
    "f24_interq_range","f25_kurtosis","f26_lempel_ziv","f27_lpcc","f28_max_frequency",
    "f29_max_power_spectrum","f30_maximum_fractal_length","f31_mean_abs_deviation",
    "f32_mean_abs_diff","f33_mean_diff","f34_median_abs_deviation","f35_median_abs_diff",
    "f36_median_diff","f37_median_frequency","f38_mfcc","f39_mse","f40_negative_turning",
    "f41_neighbourhood_peaks","f42_petrosian_fractal_dimension","f43_pk_pk_distance",
    "f44_positive_turning","f45_power_bandwidth","f46_rms","f47_skewness","f48_slope",
    "f49_spectral_centroid","f50_spectral_decrease","f51_spectral_distance","f52_spectral_entropy",
    "f53_spectral_kurtosis","f54_spectral_positive_turning","f55_spectral_roll_off",
    "f56_spectral_roll_on","f57_spectral_skewness","f58_spectral_slope","f59_spectral_spread",
    "f60_spectral_variation","f61_spectrogram_mean_coeff","f62_sum_abs_diff",
    "f63_wavelet_abs_mean","f64_wavelet_energy","f65_wavelet_entropy","f66_wavelet_std",
    "f67_wavelet_var","f68_zero_cross",
]

KEYWORD_MAP = {
    "f1_abs_energy": ["absoluteenergy", "absenergy"],
    "f2_auc": ["auc"],
    "f3_autocorr": ["autocorrelation"],
    "f4_average_power": ["averagepower"],
    "f5_calc_centroid": ["centroid"],
    "f6_calc_max": ["max"],
    "f7_calc_mean": ["mean"],
    "f8_calc_median": ["median"],
    "f9_calc_min": ["min"],
    "f10_calc_std": ["standarddeviation", "std"],
    "f11_calc_var": ["variance", "var"],
    "f12_dfa": ["dfa"],
    "f13_distance": ["distance"],
    "f14_ecdf": ["ecdf"],
    "f15_ecdf_percentile": ["ecdfpercentile"],
    "f16_ecdf_percentile_count": ["ecdfpercentilecount"],
    "f17_ecdf_slope": ["ecdfslope"],
    "f18_entropy": ["entropy"],
    "f19_fundamental_frequency": ["fundamentalfrequency", "fundamentalfreq"],
    "f20_higuchi_fractal_dimension": ["higuchi", "higuchifractaldimension"],
    "f21_hist_mode": ["histogrammode", "histmode"],
    "f22_human_range_energy": ["humanrangeenergy"],
    "f23_hurst_exponent": ["hurst"],
    "f24_interq_range": ["interquartilerange", "iqr"],
    "f25_kurtosis": ["kurtosis"],
    "f26_lempel_ziv": ["lempelziv"],
    "f27_lpcc": ["lpcc"],
    "f28_max_frequency": ["maxfrequency"],
    "f29_max_power_spectrum": ["maxpowerspectrum"],
    "f30_maximum_fractal_length": ["maximumfractallength"],
    "f31_mean_abs_deviation": ["meanabsdeviation", "mad"],
    "f32_mean_abs_diff": ["meanabsolutediff"],
    "f33_mean_diff": ["meandiff"],
    "f34_median_abs_deviation": ["medianabsdeviation"],
    "f35_median_abs_diff": ["medianabsolutediff"],
    "f36_median_diff": ["mediandiff"],
    "f37_median_frequency": ["medianfrequency"],
    "f38_mfcc": ["mfcc"],
    "f39_mse": ["mse"],
    "f40_negative_turning": ["negativeturning"],
    "f41_neighbourhood_peaks": ["neighbourhoodpeaks"],
    "f42_petrosian_fractal_dimension": ["petrosian", "petrosianfractaldimension"],
    "f43_pk_pk_distance": ["peaktopeak"],
    "f44_positive_turning": ["positiveturning"],
    "f45_power_bandwidth": ["powerbandwidth"],
    "f46_rms": ["rootmeansquare", "rms"],
    "f47_skewness": ["skewness"],
    "f48_slope": ["slope"],
    "f49_spectral_centroid": ["spectralcentroid"],
    "f50_spectral_decrease": ["spectraldecrease"],
    "f51_spectral_distance": ["spectraldistance"],
    "f52_spectral_entropy": ["spectralentropy"],
    "f53_spectral_kurtosis": ["spectralkurtosis"],
    "f54_spectral_positive_turning": ["spectralpositiveturning"],
    "f55_spectral_roll_off": ["spectralrolloff"],
    "f56_spectral_roll_on": ["spectralrollon"],
    "f57_spectral_skewness": ["spectralskewness"],
    "f58_spectral_slope": ["spectralslope"],
    "f59_spectral_spread": ["spectralspread"],
    "f60_spectral_variation": ["spectralvariation"],
    "f61_spectrogram_mean_coeff": ["spectrogrammeancoeff", "spectrogrammeancoefficient"],
    "f62_sum_abs_diff": ["sumabsolutediff"],
    "f63_wavelet_abs_mean": ["waveletabsmean"],
    "f64_wavelet_energy": ["waveletenergy"],
    "f65_wavelet_entropy": ["waveletentropy"],
    "f66_wavelet_std": ["waveletstd"],
    "f67_wavelet_var": ["waveletvar"],
    "f68_zero_cross": ["zerocrossingrate", "zerocross"],
}


def _norm(s):
    return "".join(ch for ch in str(s).lower() if ch.isalnum())


EPSILON = 1e-12


def _safe_scalar(x):
    if x is None:
        return np.nan
    if isinstance(x, (list, tuple, np.ndarray)):
        if len(x) == 0:
            return np.nan
        arr = np.asarray(x, dtype=float)
        return float(np.nanmean(arr))
    try:
        return float(x)
    except (TypeError, ValueError):
        try:
            return float(str(x).strip())
        except Exception:
            return np.nan


def _sanitize_no_zero(df):
    df = df.copy()
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.fillna(EPSILON)
    df = df.mask(df == 0, EPSILON)
    return df


def _resolve_feature_column(df_raw, target_name):
    keyword_aliases = KEYWORD_MAP.get(target_name, [])
    if not isinstance(keyword_aliases, (list, tuple, set)):
        keyword_aliases = [keyword_aliases]

    normalized_columns = {}
    for col in df_raw.columns:
        if isinstance(col, tuple):
            col_key = "_".join(map(str, col))
        else:
            col_key = str(col)
        normalized_columns[_norm(col_key)] = col

    for alias in keyword_aliases:
        norm_alias = _norm(alias)
        for norm_name, orig_name in normalized_columns.items():
            if norm_alias in norm_name or norm_name in norm_alias:
                return orig_name
    return None


def ekstrak_fitur_tsfel(nilai_array, nama_baris, fs=1, verbose_mapping=False):
    nilai_array = np.asarray(nilai_array, dtype=float)
    if len(nilai_array) == 0:
        raise ValueError(f"[{nama_baris}] array input kosong.")
    if np.std(nilai_array) == 0:
        rng = np.random.default_rng(42)
        nilai_array = nilai_array + rng.normal(0, 1e-8, size=len(nilai_array))

    frames = []
    for domain in domain_list:
        try:
            cfg_domain = tsfel.get_features_by_domain(domain)
            fitur_domain = tsfel.time_series_features_extractor(cfg_domain, nilai_array, fs=fs, verbose=0)
            fitur_domain = fitur_domain.loc[:, ~fitur_domain.columns.duplicated()]
            frames.append(fitur_domain)
        except Exception:
            continue

    if not frames:
        raise RuntimeError(f"[{nama_baris}] Ekstraksi fitur TSFEL gagal total di semua domain.")

    hasil_raw = pd.concat(frames, axis=1)
    hasil_raw = hasil_raw.loc[:, ~hasil_raw.columns.duplicated()]

    hasil = pd.DataFrame(index=[nama_baris], columns=FITUR_TARGET, dtype=float)
    for target in FITUR_TARGET:
        col_match = _resolve_feature_column(hasil_raw, target)
        if col_match is not None:
            value = _safe_scalar(hasil_raw.iloc[0][col_match])
            hasil.loc[nama_baris, target] = value
        else:
            hasil.loc[nama_baris, target] = EPSILON

    hasil = hasil.reindex(columns=FITUR_TARGET).fillna(EPSILON)
    hasil = _sanitize_no_zero(hasil)
    return hasil


rng = np.random.default_rng(42)
dates = pd.date_range("2025-08-24", "2026-08-23", freq="D")
base = {"CO": 0.032, "NO2": 0.060, "SO2": 0.020, "CH4": 0.085}
amplitudo = {"CO": 0.0035, "NO2": 0.0060, "SO2": 0.0025, "CH4": 0.0090}
noise_std = {"CO": 0.0018, "NO2": 0.0035, "SO2": 0.0015, "CH4": 0.0045}
trend_slope = {"CO": 0.001, "NO2": 0.0016, "SO2": 0.0008, "CH4": 0.0018}

raw = {"tanggal": dates}
for i, pol in enumerate(POLLUTANS):
    musiman = amplitudo[pol] * np.sin(np.linspace(0, 4 * np.pi, len(dates)) + i * 0.7)
    trend = np.linspace(0, trend_slope[pol], len(dates))
    noise = rng.normal(0, noise_std[pol], size=len(dates))
    nilai = base[pol] + musiman + trend + noise
    if pol == "CO":
        nilai[np.random.choice(len(dates), 6, replace=False)] += rng.uniform(0.015, 0.03, size=6)
    raw[pol] = nilai

df_final = pd.DataFrame(raw).set_index('tanggal')

output_dir = os.path.join(os.getcwd(), 'output_features')
os.makedirs(output_dir, exist_ok=True)

for pol in POLLUTANS:
    df_row = ekstrak_fitur_tsfel(df_final[pol].values, pol, verbose_mapping=False)
    df_row = df_row.reindex(columns=FITUR_TARGET).fillna(EPSILON)
    df_row = _sanitize_no_zero(df_row)
    out = os.path.join(output_dir, f"{pol}_features_tsfel.csv")
    df_row.to_csv(out, index=False, na_rep="1e-12", float_format="%.15g")
    print(f"saved {out}")
    print('shape=', df_row.shape)
    print('cols=', len(df_row.columns))
    print('header=', list(df_row.columns[:5]), '...', list(df_row.columns[-5:]))
    print('has_zero=', bool((df_row == 0).sum().sum()))
